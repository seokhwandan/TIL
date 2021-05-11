<template>
  <div id="parent">
    <h2>Parent</h2>
    <input type="text" v-model="parentData" @keydown.enter="sendParent">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child :appData="appData" :parentData="parentData" @send-child="getChild" />
  </div>
</template>

<script>
import Child from '@/components/Child.vue'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  components: {
    Child,
  },
  props: {
    appData: String,
  },
  methods: {
    getChild: function (data) {
      this.childData = data
      this.$emit('send-child', this.childData)
    },
    sendParent: function () {
      this.$emit('send-parent', this.parentData)
    }
  }
}
</script>

<style>
#parent {
  border: 1px solid red;
  margin: 1rem;
}
</style>