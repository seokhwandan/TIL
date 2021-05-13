<template>
  <div id="app">
    <h1>MY TODOLIST</h1>
    <p>Completed : {{ completedTodosCount }} / Uncompleted : {{ uncompletedTodosCount }}</p>
    <TodoForm/>
    <TodoList/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    // completedTodosCount: function () {
    //   return this.$store.getters.completedTodosCount
    // },
    // uncompletedTodosCount: function () {
    //   return this.$store.getters.uncompletedTodosCount
    // }
    ...mapGetters ([
      'completedTodosCount',
      'uncompletedTodosCount',
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
