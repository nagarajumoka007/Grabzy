// import { CartObject } from "./cart-oop.js";


function updateCartItemsCount(count){
    const cartElement = document.querySelector(".js-cart-count");
    cartElement.innerHTML = count;
}

function updateAddToCartButtonHtml(data){
    if(!data) return;
    const addToCartElement = document.querySelector(`.js-add-to-cart-${data.productPID}`)
    if(!addToCartElement){
        throw new Error("Exception occured while identifying the product")
    }
    if(data.productQuantity === 1){
        addToCartElement.innerHTML = `<button class="js-update-quantity update-quantity-button" data-product-id = ${data.productPID} data-sub = "true">-</button>
                                            <p class="item-quantity-${data.productPID}">${data.productQuantity}</p>
                                        <button class="js-update-quantity update-quantity-button" data-product-id = ${data.productPID} data-sub = "false">+</button>`


        addToCartElement.classList.add('cart-added-item-button')
    } else if(data.productQuantity > 1) {
        const quantityElement = document.querySelector(`.item-quantity-${data.productPID}`)
        quantityElement.innerHTML = data.productQuantity
    } else {
        addToCartElement.innerHTML = `<button class="btn add-to-cart-button js-update-quantity" data-product-id = ${data.productPID} data-sub="false">Add to cart</button>`
        addToCartElement.classList.contains('cart-added-item-button') && addToCartElement.classList.remove('cart-added-item-button')
    }
    updateCartItemsCount(data.cart_count)
}

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

async function fetchCartData(){
    try{
        const response = await fetch('/cart/details/')
        const data = await response.json()
        return data
    } catch(e){
        console.error(e)
    }
}

function updateSubtotalInPaymentUI(cart_count, amount){
    const subTotalPaymentElement = document.querySelectorAll('.subtotal-payment')
    subTotalPaymentElement.forEach((element) => {
        element.innerHTML = `Subtotal (${cart_count} items): <strong>${amount}</strong>`
    })
}

async function updateSubTotalInPayment(){
    const cart_data = await fetchCartData()
    updateSubtotalInPaymentUI(cart_data.cart_count, cart_data.amount)
}


function getCookies(name){
    let cookieValue;
    if(document.cookie && document.cookie != ''){
        const cookies = document.cookie.split(";")
        for (let i = 0; i < cookies.length; i++){
            // if(cookies[i].substring(0, name.length+1)){
            //     console.log(cookies[i].substring(0, name.length))
            // }
            if(cookies[i].trim().substring(0, name.length+1) == name + "="){
                console.log(cookies[i].trim().substring(name.length+1))
                cookieValue = decodeURIComponent(cookies[i].trim().substring(name.length+1))
                break;
            }
        }
    }

    return cookieValue;
    
}

async function updateCartQuantity(productPID, sub){
    
    try {
        const response = await fetch('/cart/add-to-cart/', {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : getCookies('csrftoken')
            },
            body : JSON.stringify({ pid : productPID, sub: sub })
        })

        if(response.redirected){
            const new_url = new URL(response.url)
            console.log(new_url.toString)
            console.log('text')
            const current_url = new URL(window.location.href)
            const search_param = current_url.searchParams.get('search')
            new_url.searchParams.set("next", window.location.pathname)
            new_url.searchParams.set('search', search_param)
            new_url.searchParams.set('pid', productPID)
            new_url.searchParams.set('sub', sub)
            new_url.searchParams.set('action', 'add_cart_item')
            window.location.href = new_url
            
        }

        if(!response.ok) {
            throw new Error(`Issue with server ${response.status}`);
        }
        const data = await response.json()
        return data;

    } catch (e) {
        alert('It seems you have not logged in, Please login or Signup..')
        }
    
}

function initCartButton(url){
    const addToCartElements = document.querySelectorAll(".js-update-quantity")
    if(url.includes('search')){
        console.log('search')
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
    } else if(url.includes('cart')){
        console.log('cart')
        const cartElement = document.querySelector(".cart-content")
        if(!cartElement) return
        cartElement.addEventListener('click', async (event) => {
        if(event.target.classList.contains('js-update-quantity')){
            const item = event.target
            const productPID = item.dataset.productId
            const sub = item.dataset.sub === 'true' ? true : false
            console.log(productPID, sub)
            const data = await updateCartQuantity(productPID, sub)
            updateCartDynamicButton(data)
            updateSubTotalInPayment()
            } else if(event.target.classList.contains('js-cartitem-delete')){
                const pid = event.target.dataset.productId
                const endpoint = `/cart/delete/${pid}/`
                const response = await fetch(endpoint)
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
    } else if(url.includes('category')){
        console.log('category')
        document.querySelector(".choose-items-grid").addEventListener('click', async (event) => {
        if(event.target.classList.contains('js-update-quantity')){
            const item = event.target
            const productPID = item.dataset.productId
            const sub = item.dataset.sub === 'true' ? true : false
            const data = await updateCartQuantity(productPID, sub)
            updateAddToCartButtonHtml(data)
            }
        })
    } else if(url.includes('product')){
        console.log('Product')
        document.querySelector(".product-container").addEventListener('click', async (event) => {
        if(event.target.classList.contains('js-update-quantity')){
            const item = event.target
            const productPID = item.dataset.productId
            const sub = item.dataset.sub === 'true' ? true : false
            const data = await updateCartQuantity(productPID, sub)
            console.log(data)
            updateAddToCartButtonHtml(data)
            } else if(event.target.classList.contains('js-buy-now')) {
                console.log('Clicked on Buy Now')
                const productPid = event.target.dataset.productId
                try{
                    const response = await fetch(`/cart/buy-now/${productPid}/`)
                    const data = await response.json()
                    updateCartItemsCount(data.cart_count)
                    window.location.href = "/cart/"
                    if(data.status !== 'success'){
                        alert("Something is wrong...")
                    }
                } catch(e) {
                    alert("Something is wrong...")
                }
                
            }
        })
    } 

}

console.log(window.location.pathname)


if(window.location.pathname === '/search/' || window.location.pathname === '/cart/' || window.location.pathname.includes('/category/') || window.location.pathname.includes('/product/') ){
    document.addEventListener('DOMContentLoaded', initCartButton(window.location.pathname));
}

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


// CartObject.updateCartNumber();