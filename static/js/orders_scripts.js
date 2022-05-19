window.onload = function(){

   let quantity, price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
   let quantity_arr = []
   let price_arr = []

   let total_forms = parsInt($('input[name=orderitems-TOTAL_FORMS]').val())
   console.log(total_forms)

   let order_total_cost = parsInt($('.order_total_cost').text().replace(',','.')) || 0;
   let order_total_quantity = parsInt($('.order_total_cost').text()) || 0;


   for(let i = 0; i < total_forms; i++){
        quantity = parsInt($('input[name=orderitems-' + i + '-quantity]').val())
        price = parsInt($('.orderitems-' + i + '-price]').text().replace(',','.'))

        quantity_arr[i] = quantity;
        if(price){
            price_arr[i] = price

        }else {
            price[i] = 0;
        }
   }

   // method => 1
   $('order_form').on('click', 'input[type=number]', function(){
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-','').replace('-quantity'))
        if(price_arr[orderitem_num]){
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num]
            quantity_arr[orderitem_num] = orderitem_quantity
            orderSummaryUpdate(price[orderitem_num], delta_quantity)


        }
        console.log(target)

   })



   // method => 2
      $('order_form').on('click', 'input[type=number]', function(){
        let target = event.target;
        console.log(target)
        orderitem_num = parseInt(target.name.replace('orderitems-','').replace('-DELETE', ''))
        if(target.checked){
                delta_quantity = -quantity_arr[orderitem_num]
        }else{
            delta_quantity = quantity_arr[orderitem_num]
        }

        console.log(target)

   })

   console.info( 'QUANTITY', quantity_arr)
   console.info( 'PRICE', price_arr)
   console.log(order_total_cost, order_total_quantity)



   function orderSummaryUpdate(orderitem_price, delta_quantity){
        delta_cost = orderitem_price*delta_quantity;
        order_total_cost = Number((order_total_cost+delta_cost)toFixed(2))
        order_total_quantity = order_total_quantity+delta_quantity;
        $('.order_total_quantity').html(order_total_quantity.toString());
        $('.order_total_cost').html(order_total_cost.toString()+',00');
   }



    $('.formset-row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить продукт',
        prefix: 'orderitems',
        removed: deleteOrderItem,
    })

   function deleteOrderItem(row){
        let target_name = row[0].querySelector('input[type="number"]').name
        orderitem_num = parseInt(target_name.replace('orderitems-','').replace('-quantity', ''))
        delta_quantity = -quantity_arr[orderitem_num]
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity)
   }


}