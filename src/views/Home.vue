<template>

  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
    <!-- <TodoItem v-for="(item, index) in todoList " : /> -->
    <Add :handlePlus="handlePlus"/>
    <TodoItem v-for="(item, index) in todoList" :todo="item" :index="index" :key="index" :handleMinus="handleMinus"/>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs} from 'vue';

import TodoItem from '../components/TodoItem.vue' 
import { dataInterface } from '../types/types'
import Add from '../components/Add.vue'
// import Buttom from '../components/Buttom.vue'

// export default defineComponent({
//   name: 'Home',
//   components: {
//     HelloWorld,
//   },
// });
   export default defineComponent({
     name: 'Home',
     components:{
       TodoItem,
        Add,
     },
     setup() {
      // const test = ref('11')
      const data = reactive<dataInterface>({
           todoList: [],
           handleMinus: (index) => {
             data.todoList.splice(index, 1)
           },
           handlePlus: (value) => {
             data.todoList.push(value)
            //  test.value=value
            // console.log(value)
            // console.log(value)
           }
         })
         return{
           ...toRefs(data),
         }
         
     }
   })
</script>
