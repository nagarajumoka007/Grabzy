import { updateCartItemsCount, updateCartQuantity, makeAPICall } from "../../../../static/JavaScript/utils.js"

function updateCartDynamicButton(data){
    if(!data) return;
    if(data.productQuantity === 0){
        const cartButtonElement = document.querySelector(`.js-cart-grid-${data.productPID}`)
        cartButtonElement.remove()
        const horizontalLine = document.querySelector(`.js-horizontal-line-${data.productPID}`)
        if(horizontalLine) horizontalLine.remove()
        const cartContentElement = document.querySelector('.js-cart-content')
        if(data.cart_count === 0 && cartContentElement){
            cartContentElement.classList.add('empty-cart-container')
            cartContentElement.classList.remove('cart-content')
            cartContentElement.innerHTML = `<p class="cart-empty-text">Your cart is empty</p>`
        }
    } else{
        const quantityElement = document.querySelector(`.js-cart-item-quantity-${data.productPID}`)
        quantityElement.innerHTML = data.productQuantity
    }
    updateCartItemsCount(data.cart_count)

}

function updateSubtotalInPaymentUI(cart_count, amount){
    const subTotalPaymentElement = document.querySelectorAll('.subtotal-payment')
    subTotalPaymentElement.forEach((element) => {
        element.innerHTML = `Subtotal (${cart_count} items): <strong>${amount}</strong>`
    })
}

async function updateSubTotalInPayment(){
    const response = await makeAPICall('/cart/details/', "GET")
    const cart_data = await response.json()
    console.log("API Call is working", cart_data)
    updateSubtotalInPaymentUI(cart_data.cart_count, cart_data.amount)
}


const cartElement = document.querySelector(".cart-content")
cartElement.addEventListener('click', async (event) => {
if(event.target.classList.contains('js-update-quantity')){
    const item = event.target
    const productPID = item.dataset.productId
    const sub = item.dataset.sub === 'true' ? true : false
    const data = await updateCartQuantity(productPID, sub)
    updateCartDynamicButton(data)
    updateSubTotalInPayment()
    } 
    
    else if(event.target.classList.contains('js-cartitem-delete')){
        const pid = event.target.dataset.productId
        const endpoint = `/cart/delete/${pid}/`
        const response = await makeAPICall(endpoint, 'GET')
        const data = await response.json()
        const cartItemElement = document.querySelector(`.js-cart-grid-${pid}`)
        cartItemElement.remove()
        const horizontalLine = document.querySelector(`.js-horizontal-line-${pid}`)
        horizontalLine.remove()
        const cartContentElement = document.querySelector('.js-cart-content')
        if(data.cart_count === 0 && cartContentElement){
            cartContentElement.classList.add('empty-cart-container')
            cartContentElement.classList.remove('cart-content')
            cartContentElement.innerHTML = `<p class="cart-empty-text">Your cart is empty</p>`
        }
        updateSubTotalInPayment()
        updateCartItemsCount(data.cart_count)

    }
})

updateSubTotalInPayment()