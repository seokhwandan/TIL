<template>
  <div>
    <h2>Add Todos</h2>
    <input type="text" v-model="todoTitle" @keydown.enter="createTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        completed: false,
      }
      if (todoItem.title.trim()) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = ''
    }
  }
}
</script>

<style>

</style>