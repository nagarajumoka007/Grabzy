import { updateCartQuantity, 
    updateAddToCartButtonHtml, makeAPICall, updateCartItemsCount } from "../../../../static/JavaScript/utils.js"



document.querySelector(".product-container").addEventListener('click', async (event) => {
if(event.target.classList.contains('js-update-quantity')){
    const item = event.target
    const productPID = item.dataset.productId
    const sub = item.dataset.sub === 'true' ? true : false
    const cartUpdateResponse = await updateCartQuantity(productPID, sub)
    updateAddToCartButtonHtml(cartUpdateResponse)
    } else if(event.target.classList.contains('js-buy-now')) {
        const productPid = event.target.dataset.productId
        try{
            const response = await makeAPICall(`/cart/buy-now/${productPid}/`, 'GET')
            const data = await response.json()
            updateCartItemsCount(data.cart_count)
            window.location.href = "/cart/"
            if(data.status !== 'success'){
                alert("Something is wrong...")
            }
        } catch(e) {
            alert("Exception occured while calling an API: ", e)
        }
        
    }
})