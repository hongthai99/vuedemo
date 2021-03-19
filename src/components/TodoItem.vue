<template>
   <header>
       <!-- <h1>{{title}}</h1> -->
       <!-- <Buttom text="Add" color="green"/> -->
       <!-- <Buttom/> -->
       <div class="todoitem-wrap">
         <div class="todoitem"> {{index+1}}.  {{todo}}</div>
         <div class="checkoutitem">
           <div class="del-btn" @click="deleteTodo(index)"> DELETE</div>
         </div>
       </div>
   </header>
</template>


<script lang="ts">

import {defineComponent} from 'vue'
// import Buttom from './Buttom.vue'

// import Buttom from './Buttom'

export default defineComponent ({
  // components: {  },
  //   name: 'TodoItem',
  //   // props:{
  //   //   title: String,
  //   // },
  //   props: {
  //     title: {
  //       type: String
  //     }
  //   }
  //   // components:{
  //   //   Buttom,
  //   // }
  
  name: 'todoItem',
  props: {
    todo: String,
    index: Number,
    handleMinus: {
      type: Function,
      required: true
    },
  },
  setup(props){
    const deleteTodo = (index: number) => {
            props.handleMinus(index)
        }
        return {
            deleteTodo
        }
  }
  })
</script>


<style>
  .todoitem-wrap{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 10px;
    background-color: #e9e9e9;
    margin: 10px 0;
    border-radius: 6px;
  }
  .mr20{
    margin-right: 20px;
  }
  .checkoutitem{
    display: inline-flex;
    align-items: center;
  }

</style>