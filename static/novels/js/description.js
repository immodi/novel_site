const currentUrl = window.location.href
const urlTextToArrayLength = currentUrl.split("/").length - 1
const currentPageNumber = parseInt(currentUrl.split("/")[urlTextToArrayLength])

let currentPageNumberInList = Array.from(document.querySelector(".novels-total").children)

if (currentPageNumber === 1 || isNaN(currentPageNumber)) {
    currentPageNumberInList = currentPageNumberInList[1]
} else {
    currentPageNumberInList = currentPageNumberInList[2]
}

currentPageNumberInList.classList.toggle("selected")