import { updateCartQuantity, 
    updateAddToCartButtonHtml, 
    handleEmptySearch} from "../../../../static/JavaScript/utils.js"


const searchInputElement = document.querySelector('.js-search-input')
searchInputElement.value = new URL(window.location.href).searchParams.get('search')
document.querySelector(".choose-items-grid").addEventListener('click', async (event) => {
if(event.target.classList.contains('js-update-quantity')){
    const item = event.target
    const productPID = item.dataset.productId
    const sub = item.dataset.sub === 'true' ? true : false
    const data = await updateCartQuantity(productPID, sub)
    updateAddToCartButtonHtml(data)
    }
})

handleEmptySearch()