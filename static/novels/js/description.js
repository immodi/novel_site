// const pageNumbersList = document.querySelector(".novels-total")
// const pageNumbersArray = Array.from(pageNumbersList.children)
// let currentPageNumberRightIndex = 2

// localStorage.clear()
// pageNumbersArray.forEach((num) => {num.style.display = 'none'})
// pageNumbersArray[parseInt(localStorage.getItem("firstIndex")) || 0].style.display = 'flex'
// pageNumbersArray[parseInt(localStorage.getItem("secondIndex")) || 1].style.display = 'flex'

// function moveRight() {
//     try {
//         pageNumbersArray[currentPageNumberRightIndex].style.display = 'flex'
//         pageNumbersArray[currentPageNumberRightIndex - 2].style.display = 'none'
//         currentPageNumberRightIndex++
//         savePageNumState(currentPageNumberRightIndex-2, currentPageNumberRightIndex-1)
//     } catch (error) {
//         return
//     }
// }

// function savePageNumState(leftIndex, rightIndex) {
//     localStorage.setItem("firstIndex", leftIndex)
//     localStorage.setItem("secondIndex", rightIndex)
// }