<template>
  <!-- <button class="btn">{{text}}</button> -->
  <div class="input-wrap">
    <input type="text" class="input" 
      @keyup.enter="addTodo(todoValue)" v-model="todoValue">
    <div class="btn-add" @click="handlePlus(todoValue)">
      ADD
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, toRefs } from "vue";

// import Button from '../../../task/src/components/Button.vue'
export default defineComponent ({
  name: 'addTodoItem',
  props: {
    handlePlus: {
      type: Function,
      required: true,
    }
  },
  setup(props){
    // const todoValue = ref('')
    const data = reactive({
      todoValue: '',
      addTodo: (value: string) => {
        props.handlePlus(value),
        data.todoValue = ''
        // console.log(value)
      }
    })
    // console.log(data)
    return{
      ...toRefs(data)
    }
    
    
  }
})
</script>

<style>
  .input{
    width: 260px;
    height: 35px;
    margin-right: 10px;
    border-color: #e5e5e5;
    box-sizing: border-box;
    border-radius:4px;
    border:1px solid #c8cccf;
    color:#6a6f77;
    -web-kit-appearance:none;
    -moz-appearance: none;
    outline:0;
    text-decoration:none;
  }
  .btn-add{
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    background: #fff;
    border: 1px solid #dcdfe6;
    color: #fff;
    background-color: #409eff;
    border-color: #409eff;
    -webkit-appearance: none;
    text-align: center;
    box-sizing: border-box;
    outline: none;
    margin: 0;
    transition: .1s;
    font-weight: 500;
    /* -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none; */
    padding: 8px 15px;
    font-size: 14px;
    border-radius: 4px;
  }
  
</style>