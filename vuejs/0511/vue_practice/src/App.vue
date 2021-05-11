<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- v-bind:내려보내는이름="내려보내는값" -->
    <Parent :appData="appData" @send-parent="getParent" @send-child="getChild" />
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'

export default {
  name: 'App',
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  components: {
    Parent,
  },
  methods: {
    getParent: function (data) {
      this.parentData = data
    },
    getChild: function (data) {
      this.childData = data
    }
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

  width: 500px;
  border: 1px solid black;
  margin: 60px auto 0px;
}
</style>
