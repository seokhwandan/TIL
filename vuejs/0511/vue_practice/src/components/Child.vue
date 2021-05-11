<template>
  <div id="child">
    <h2>Child</h2>
    <input type="text" @keydown.enter="inputChild">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: String,
    parentData: String,
  },
  data: function () {
    return {
      childData: '',
    }
  },
  methods: {
    inputChild: function () {
      // console.log(event)
      this.childData = event.target.value
      this.$emit('send-child', this.childData)
    }
  }
}
</script>

<style>
#child {
  border: 1px solid blue;
  margin: 1rem;
}
</style>