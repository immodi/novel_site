const novelsNames = document.querySelectorAll(".novel-name")
let maxNovelTitleCharacters = 40
if (window,innerWidth > 1100) {
    maxNovelTitleCharacters = 30
}

novelsNames.forEach(name => {
    if (name.innerHTML.length < maxNovelTitleCharacters) {
        return
    } else {
        name.innerHTML = name.innerHTML.slice(0, maxNovelTitleCharacters-1) + "..."
    }
});

