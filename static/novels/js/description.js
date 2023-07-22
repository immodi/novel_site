const currentUrl = window.location.href
const currentPageNumber = parseInt(currentUrl.slice(currentUrl.length - 1, currentUrl.length))

let currentPageNumberInList = Array.from(document.querySelector(".novels-total").children)

if (currentPageNumber === 1 || isNaN(currentPageNumber)) {
    currentPageNumberInList = currentPageNumberInList[0]
} else {
    currentPageNumberInList = currentPageNumberInList[1]
}

currentPageNumberInList.classList.toggle("selected")