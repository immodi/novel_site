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


// window.scrollTo(0, 0)

// let navWrapper = document.querySelector(".nav-wrapper")
// let novelsTotal = document.querySelector(".novels-total")
// let pageNumbers = document.querySelectorAll(".page-number")
// let covers = [...document.querySelectorAll(".novel-cover")]
// let main = document.querySelector("main")

// let lastCoverLeft = covers[2].getBoundingClientRect().left 
// let coverHeight = covers[2].getBoundingClientRect().height 
// let lastCoverTop = covers[2].getBoundingClientRect().top 

// if (isNumeric(window.location.href.slice(-1))) {
//     pageNumbers[window.location.href.slice(-1) - 1].classList.toggle("selected")
// } else {
//     pageNumbers[0].classList.toggle("selected")
// }
// function isNumeric(str){
//     return /^\d+$/.test(str);
// }