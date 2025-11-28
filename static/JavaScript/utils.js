export function updateCartItemsCount(count){
    const cartElement = document.querySelector(".js-cart-count");
    cartElement.innerHTML = count;
}

export function updateAddToCartButtonHtml(data){
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

// export function updateCartDynamicButton(data){
//     if(!data) return;
//     if(data.productQuantity === 0){
//         const cartButtonElement = document.querySelector(`.js-cart-grid-${data.productPID}`)
//         cartButtonElement.remove()
//         const horizontalLine = document.querySelector(`.js-horizontal-line-${data.productPID}`)
//         if(horizontalLine) horizontalLine.remove()
//         const cartContentElement = document.querySelector('.js-cart-content')
//         if(data.cart_count === 0 && cartContentElement){
//             cartContentElement.classList.add('empty-cart-container')
//             cartContentElement.classList.remove('cart-content')
//             cartContentElement.innerHTML = `<p class="cart-empty-text">Your cart is empty</p>`
//         }
//     } else{
//         const quantityElement = document.querySelector(`.js-cart-item-quantity-${data.productPID}`)
//         quantityElement.innerHTML = data.productQuantity
//     }
//     updateCartItemsCount(data.cart_count)

// }

export async function makeAPICall(endpoint, method, body=null, headers={}){
    try{
        if(method === "POST"){
            const response = await fetch(endpoint, {
                method: method,
                body: body,
                headers: headers
            })
            return response
        } else if(method === "GET"){
            const response = await fetch(endpoint, {
                method: method,
                headers: headers || {}
            })
            return response
        }
        
    } catch(e){
        console.log(e)
    }
}

export function getCookies(name){
    let cookieValue;
    if(document.cookie && document.cookie != ''){
        const cookies = document.cookie.split(";")
        for (let i = 0; i < cookies.length; i++){
            if(cookies[i].trim().substring(0, name.length+1) == name + "="){
                console.log(cookies[i].trim().substring(name.length+1))
                cookieValue = decodeURIComponent(cookies[i].trim().substring(name.length+1))
                break;
            }
        }
    }

    return cookieValue;
    
}

export async function updateCartQuantity(productPID, sub){
    
    try {
        const headers = {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : getCookies('csrftoken')
            }

        const body = JSON.stringify({ pid : productPID, sub: sub })
         
        const response = await makeAPICall('/cart/add-to-cart/', 'POST', body ,headers)

        if(response.redirected){
            const new_url = new URL(response.url)
            alert("It seems you have not logged In. Please login or Signup")
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
        console.log("Exception while calling an API: ", e)
        }
    
}