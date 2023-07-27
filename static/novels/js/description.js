const currentUrl = window.location.href
const currentPageNumber = parseInt(currentUrl.split("/")[5])

let currentPageNumberInList = Array.from(document.querySelector(".novels-total").children)

if (currentPageNumber === 1 || isNaN(currentPageNumber)) {
    currentPageNumberInList = currentPageNumberInList[1]
} else {
    currentPageNumberInList = currentPageNumberInList[2]
}

currentPageNumberInList.classList.toggle("selected")