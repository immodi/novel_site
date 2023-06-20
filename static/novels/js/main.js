window.scrollTo(0, 0)

let navWrapper = document.querySelector(".nav-wrapper")
let novelsTotal = document.querySelector(".novels-total")
let pageNumbers = document.querySelectorAll(".page-number")
let covers = [...document.querySelectorAll(".novel-cover")]
let main = document.querySelector("main")

let lastCoverLeft = covers[2].getBoundingClientRect().left 
let coverHeight = covers[2].getBoundingClientRect().height 
let lastCoverTop = covers[2].getBoundingClientRect().top 

// novelsTotal.style.width = `${pageNumbers.length * 30}px`
// navWrapper.style.width = (lastCoverLeft + coverHeight + 50) + "px"
// main.style.width = (lastCoverLeft + coverHeight + 50) + "px"
// main.style.height = (covers[covers.length-1].getBoundingClientRect().top + coverHeight + 200) + "px"

if (isNumeric(window.location.href.slice(-1))) {
    pageNumbers[window.location.href.slice(-1) - 1].classList.toggle("selected")
} else {
    pageNumbers[0].classList.toggle("selected")
}

// if (window.innerWidth >= 1200) {
//     navWrapper.style.width = "100vw"
//     main.style.width = "100vw"
//     main.style.height = "315vh"
// } 
// else if (window.innerWidth < 695 && parseInt(pageNumbers[pageNumbers.length-1].innerHTML) == parseInt(window.location.href.slice(-1))) {
//     main.style.height = ((covers[covers.length-1].getBoundingClientRect().top + coverHeight) * 2) + "px"
// }

function isNumeric(str){
    return /^\d+$/.test(str);
}
