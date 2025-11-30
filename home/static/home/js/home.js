import {updateCartQuantity,
    updateAddToCartButtonHtml, 
    handleEmptySearch } from "../../../../static/JavaScript/utils.js"


const homePageElement = document.querySelector(".scrollabale-items-grid")
if(homePageElement){
    document.querySelector(".scrollabale-items-grid").addEventListener('click', async (event) => {
        if(event.target.classList.contains('js-update-quantity')){
            const item = event.target
            const productPID = item.dataset.productId
            const sub = item.dataset.sub === 'true' ? true : false
            const data = await updateCartQuantity(productPID, sub)
            console.log(data)
            updateAddToCartButtonHtml(data)
            }
        })
}

handleEmptySearch()