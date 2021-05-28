<template>
  <div>
  <button v-if="!showForm" @click="showForm=true">Subscribe to Updates</button>
  <form v-else style="flip-enter-active" onsubmit="return false">
    <input  class='text-input' v-model="email" placeholder="Your Email">
    <input class='button' type="submit" value="Get Updates" @click="post_data"/>
    <label> {{ message }} </label>
  </form>
    </div>
</template>

<script>
const axios = require('axios');

module.exports = {
  
  props: ['appCode'],
  data: function() {
    return {
      showForm: false,
      email: "",
      message: ""
    }
  },
  methods: {
    post_data(){
      this.message='⏳'
      console.log(this.appCode)
      console.log(this.email)
      axios.post("https://api.releasechannel.com/subscribe", {
        data: {
          "email": this.email,
          "application": this.appCode
          },
        headers: {
          "Content-Type":"application/json"
        }
      })
      .then(response => (this.message = '✅'))
      .catch(response => (this.message = '🚫'))
    }
  }
}
</script>

<style scoped>
form input.text-input{
  cursor: text;
    width: 10rem;
    height: 2rem;
    color: #4e6e8e;
    display: inline-block;
    border: 1px solid #cfd4db;
    border-radius: 2rem;
    font-size: 0.9rem;
    line-height: 2rem;
    padding: 0 0.8rem 0 0.8rem;
    outline: none;
    transition: all 0.2s ease;
    background: #fff;
    background-size: 1rem;
}

form input.button {

    height: 2rem;
    display: inline-block;
    font-size: 0.9rem;
    color: #fff;
    background-color: #3eaf7c;
    padding: 0 0.8rem 0 0.8rem;
    border-radius: 2rem;
    transition: background-color 0.1s ease;
    box-sizing: border-box;
    border: 0;
    border-bottom: 1px solid #389d70;
}

button {
    display: inline-block;
    font-size: 1.0rem;
    color: #fff;
    background-color: #3eaf7c;
    padding: 0.8rem 0.8rem;
    border-radius: 4px;
    transition: background-color 0.1s ease;
    box-sizing: border-box;
    border: 0;
    border-bottom: 1px solid #389d70;
}

button:focus {
    background-color: #226346;
}

p {
  font-size: 2em;
  text-align: center;
}
</style>

