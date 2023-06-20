const searchArea = document.querySelector("#searchArea");
const searchIcon = document.querySelector(".search-svg");
const novelList = document.querySelector(".novels-list");

let typingTimer; //timer identifier
let doneTypingInterval = 300; //time in ms
let globalSearchEvent;

searchArea.addEventListener("keyup", (e) => {
  globalSearchEvent = e
  clearTimeout(typingTimer);
  if (searchArea.value) {
    typingTimer = setTimeout(() => {
      doneTyping(e);
    }, doneTypingInterval);
  }
});

searchArea.addEventListener("keydown", (e) => {
  globalSearchEvent = e
  if (e.keyCode == 13) {
    e.preventDefault();
    clearTimeout(typingTimer);
    if (searchArea.value) {
      typingTimer = setTimeout(() => {
        doneTyping(e);
      }, 0);
    }
  }
});

searchIcon.addEventListener("click", () => {
  clearTimeout(typingTimer);
  if (searchArea.value) {
    typingTimer = setTimeout(() => {
      doneTyping(globalSearchEvent);
    }, 0);
  }
})

function doneTyping(event) {
  let novelName = event.target.value;
  novelName = novelName.replace(/(\r\n|\n|\r)/gm, "");

  fetch("/search-novel", {
    body: JSON.stringify({ name: novelName }),
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => {
      let novelData = Object.values(data)[0];
      let sectionNodes = "";
      if (novelData.length == 0) {
        sectionNodes = `<h3 class="no-novels">No novel could be found.</h3>`;
      } else {
        novelData.forEach((i) => {
          let novelName;
          if (i[0].length < 40) {
            novelName = i[0]
          } else {
            novelName = i[0].slice(0, 39) + "..."
          }
          sectionNodes = sectionNodes + 
          `
          <li class="novel-item w-3/4 mt-4 mb-4 pt-4">
            <a href="/novel?novel_name=${i[0]}" class="novel-item">
              <img src="${i[1]}" class="novel-cover w-32 h-38 rounded-sm relative left-0">
              <div class="novel-description">
                <p class="novel-name text-sm mt-4 mb-1 font-medium relative left-0">${novelName}</p>
                <p class="novel-chapter-no text-xs relative font-medium left-0">${i[2]} Chapters</p>
              </div>
            </a>
          </li>
          `;
        });
      }
      
      novelList.innerHTML = sectionNodes;
    });
}
