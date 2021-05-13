import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    todos: [],
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, deleteTodo) {
      // const index = state.todos.indexOf(todoItem)
      // state.todos.splice(index, 1)

      // state.todos = state.todos.filter(todo => {
      //   return todo !== todoItem
      // })

      state.todos = deleteTodo
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          return { ...todo, completed: !todo.completed }
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    // deleteTodo: function ({ commit }, todoItem) {
      // commit('DELETE_TODO', todoItem)
      
    deleteTodo: function (context, todoItem) {
      const deleteTodo = context.state.todos.filter(todo => {
        return todo !== todoItem
      })
      context.commit('DELETE_TODO', deleteTodo)
    },
    updateTodo: function ({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    }
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    }
  },
  modules: {
  }
})
