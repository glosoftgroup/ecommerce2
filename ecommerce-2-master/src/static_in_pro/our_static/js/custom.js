(function($){
    /* calls when the dom is ready */
   // showSomething();
   updateCartItemCount();
   updateMinicart();

   /*--- 
     ** - item detail page
    ---*/
    /* add to cart button*/
    $(".btn-add-cart").click(function(){
        var formData = $("#add-form").serialize();
        console.log(formData);
        $.ajax({
            type: "GET", // "POST"
            url: "/cart/",
            data: formData,
            success: function(data) {
                updateCartItemCount();
                updateMinicart();
                toastr.success(data.flash_message, 'Success', 
                { showDuration: 2000,hideDuration: 1000, timeOut: 2000});
            }, 
            error: function(response, error) {
                console.log(error)
            }
        });

    });
    /* end to cart button */
    /* -- end detail page -- */
})(jQuery);

/* ---------------------------------------------
                Common
     --------------------------------------------- */
/*--- about us function ---*/
function showSomething(id){
    alert(id);
}
/*--- update cart item---*/
function updateCartItemCount(){
    var badge = $("#notify");
    var my_count = $("#my-count");

    $.ajax({
        type: "GET",
        url: "/cart/count/",
        success: function(data){
            badge.text(data.count);
            console.log(data.count);
            console.log('cart is '+ data.cart_id);
            my_count.text(data.count);
            /**- if cart qty is 0-**/
            if(data.count == 0){
              $('.cart-block-content').fadeOut(function(){
                $('.cart-block-content').html('Cart is empty').fadeIn();
              });
            }
        },
        error: function(error) {
            console.log(error);
        }

    });

 }

 /*--- update minicart ---*/
function updateMinicart(){      
    $(".cart-block").html('&nbsp;').load("/minicart/");
}

/*--- delete minicart item ---*/
function removeCartItem(id){
    $.ajax({
        type: "GET",
        url: "/cart/",
        data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                item: id,
                qty:1,
                delete:'True'
        },
        success: function(data){
            var item_id = $(".remove-item-"+id);
            item_id.fadeOut(function(){
                updateCartItemCount();
                $('.total-price').html(data.subtotal);
            });
            /* also remove from the cart table */
            var item = $("#productItem-"+id);
                item.addClass( "animated bounceOut");
                item.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
                    $(this).remove();
                  if (data.deleted){
                    $("#st").text(data.subtotal);
                    $("#tt").text(data.tax_total);
                    $("#ct").text(data.cart_total);
                  }
                });
                if (data.total_items == 0 ) {
                    item.addClass( "animated bounceOut");
                    item.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
                        $(this).remove();
                        $(".shopping-cart").fadeOut();
                        $(".main-content").html('&nbsp;').load("/emptycart/");
                    });

                }
            /* end remove from cart table */

            // alert('deleted')
            console.log('deleted');
        },
        error: function(error) {
            console.log(error);
        }

    });
}

/* ---------------------------------------------
                Home
     --------------------------------------------- */
     /* add to cart */
     function addTocart(id, name, imageurl, id2){
        var item_name = name;
        var imagepath = imagepath;
        $.ajax({
            type: "GET", // "POST"
            url: "/cart/",
            data: {
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    item: id2,
                    qty:1
            },
            success: function(data){
                updateCartItemCount();
                updateMinicart();
                $('.p-message').html(data.flash_message);
                $('.p-namex').html('Name: '+ name);
                $('.p-imagex').attr('src', imageurl);
                $('.p-price').html('Price: KShs'+ data.line_total);
                $('.p-quantity').html('Qty: '+data.item_quantity);

                $('#myModal').modal();
                toastr.success(data.flash_message, 'Success', { showDuration: 2000,hideDuration: 1000, timeOut: 2000,});           
            }, 
            error: function(error) {
                // console.log(response)
                console.log(error);
                toastr.error('cannot process', 'Error', {timeOut: 500});
            }
        });        
    }