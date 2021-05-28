

<template>
  <form onsubmit="return false">
    <input v-model="email" placeholder="Add email to receive updates">
    <input type="submit" @click="post_data"/>
    <label> {{ message }} </label>
    </form>
    
</template>

<script>
const axios = require('axios');

module.exports = {
  
  props: ['appCode'],
  data: function() {
    return {
      email: "Your Email",
      message: "Trying"
    }
  },
  methods: {
    post_data(){
      
      console.log(this.appCode)
      console.log(this.email)
      axios.get("https://api.releasechannel.com", {
        headers: {"Access-Control-Allow-Origin": "*"}
      })
      .then(response => (this.message = response.data))
    }
  }
}
</script>

<style scoped>
p {
  font-size: 2em;
  text-align: center;
}
</style>

