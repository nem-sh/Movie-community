<template>
  <div id="app"  style="height:100%; background-color : black;">
    <div class="fixed-top">
      <nav :class="{ 'bg-danger' : color==1, 'bg-purple':color==2,'bg-primary':color==3,'bg-warning':color==4}" class="navbar navbar-expand-lg text-decoration-none p-0" >
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse " id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link text-black-50 pt-0 pb-0 " v-if="!isLoggedIn" :to="{name: 'Login'}" style="font-family: 'Staatliches', cursive;">Login</router-link> 
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-black-50 pt-0 pb-0" v-if="!isLoggedIn" :to="{name: 'Signup'}" style="font-family: 'Staatliches', cursive;">Signup</router-link>
          </li>
       

          <li class="nav-item" v-if="isLoggedIn" >
            <a class="nav-link text-black-50 pt-0 pb-0 m-0"  @click="myProfile" style="font-family: 'Staatliches', cursive; margin-bottom:0px;">Profile</a>
          </li>
          <li class="nav-item">
          
            <router-link class="nav-link text-black-50 pt-0 pb-0" v-if="isLoggedIn" :to="{name: 'Logout'}" @click.native="logout" style="font-family: 'Staatliches', cursive;">Logout</router-link>
          </li>
        </ul>
    </div>
    </nav>
    <nav :class="{ 'bg-red' : color==1, 'bg-violet' :color==2,'bg-info':color==3,'bg-yellow':color==4}" class="navbar navbar-expand-lg text-decoration-none">
      <router-link class="ml-5 navbar-brand text-white font-weight-bold f-b" :to="{name: 'MovieList'}" style="font-family: 'Staatliches', cursive;">Movie App</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse main-bar" id="navbarSupportedContent">
        <ul class="navbar-nav  nav-pad">
          <li class="nav-item">
            <router-link class="nav-link font-weight-bold text-white f-b" :to="{name: 'community'}" style="font-family: 'Staatliches', cursive;">community</router-link> 
          </li>
          <li class="nav-item">
            <router-link class="nav-link font-weight-bold text-white f-b" :to="{name: 'movie'}" style="font-family: 'Staatliches', cursive;">movie</router-link>
          </li>
                   
        </ul>
         <div class="searchbar">
            <input class="search_input" type="text" name="" placeholder="Search..." v-model="searchData.searchValue">
            <a @click="search" class="search_icon"><i class="fas fa-search"></i></a>
          </div>
    </div>
    </nav>

    </div>
    
    
    <router-view 
      @submit-login-data="login" 
      @submit-signup-data="signup" 
      @submit-review-create-data="reviewCreate" 
      @submit-review-delete-data="reviewDelete"
      @change-color-P="changeColorP"
      
      @change-color-M="changeColorM"
      @change-color-y="changeColorY"
      @change-color-R="changeColorR"
      :myInformation = "myInformation"
      :isLoggedIn ="isLoggedIn"
      :searchResultData="searchResultData"
    />
  </div>


</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',

  data: function () {
    return {
      color: 1,
      isLoggedIn:false,
      searchData:{
        searchValue: '',
      },
      searchResultData:{
        reviews:null,
        movies:null,
        users:null,
      },
      myInformation : null,
    }
  },

  methods: {
    getUser: function(){
      if (this.isLoggedIn){
        const axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
                }
      axios.post(`${BACK_URL}/boards/user/`, null,axiosConfig)
        .then((response)=>{
            console.log(response.data)

            this.myInformation = response.data
            
          })
          .catch((error)=>{
            console.log(error.response)
            alert(error.response.data.non_field_errors[0])
          })

      }
      
    },
    setCookiesAndLogin: function (key) {
      this.$cookies.set('auth-token', key)
      this.isLoggedIn = true
      
      this.getUser()
      this.$router.push('/boards/')
    },
    login: function (loginData) {
      console.log(loginData)
      axios.post(`${BACK_URL}/rest-auth/login/`, loginData)
        .then((response)=>{
          console.log(response.data)
          this.setCookiesAndLogin(response.data.key)
          
        })
        .catch((error)=>{
          console.log(error.response)
          alert(error.response.data.non_field_errors[0])
        })
    },
    logout: function () {
      console.log('logout')
      const axiosConfig = {
        headers:{
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        },
      }
      axios.post(`${BACK_URL}/rest-auth/logout/`, null, axiosConfig)
        .then((response)=> {
          console.log(response)
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.myInformation = null
          
      this.$router.push('/boards/')
        })
        .catch((error)=>{
          console.log(error)
        })
        
    },
    signup: function (signupData) {
      axios.post(`${BACK_URL}/rest-auth/signup/`, signupData)
        .then((response) => {         
          this.setCookiesAndLogin(response.data.key)
        })
        .catch((error) => {
          alert(error.response.data.username, error.response.data.password)
        })
    },


    reviewCreate: function (reviewCreateData) {
      
      console.log(reviewCreateData)
      if (this.isLoggedIn){
        const axiosConfig = {
          headers:{
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          },
        }
      console.log(reviewCreateData)
      axios.post(`${BACK_URL}/boards/${reviewCreateData.movie}/review_create/`, reviewCreateData, axiosConfig)
        .then((response) => {
          console.log(response)
          alert('작성했습니다^^')
          this.$router.push(`/boards/${reviewCreateData.movie}/${response.data.id}/`)
        })
        .catch((error) => {
          console.log(error.response)
          alert('다시 작성하도록!')
        })
      } else {
        alert('먼저 로그인을 해주세요')
        
      }

      
    },
    reviewDelete: function (reviewDeleteData) {
      
        console.log(reviewDeleteData)
        if (this.isLoggedIn){
          const axiosConfig = {
            headers:{
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            },
          }
          this.$router.push(`/boards/${reviewDeleteData.movie}/`)
          console.log('bi')
          axios.post(`${BACK_URL}/boards/${reviewDeleteData.movie}/${reviewDeleteData.review}/review_delete/`, reviewDeleteData, axiosConfig)
            .then(() => {
              this.$router.push(`/boards/${reviewDeleteData.movie}/`)
            })
            .catch((error) => {
              console.log(error.response)
              alert(error[0])
            })
        } else {
          alert('먼저 로그인을 해주세요')
          
        }

      
    },
    reviewUpdate: function (reviewUpdateData) {
      
        console.log(reviewUpdateData)
        if (this.isLoggedIn){
          const axiosConfig = {
            headers:{
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            },
          }
          console.log('bi')
          axios.post(`${BACK_URL}/boards/${reviewUpdateData.movie}/${reviewUpdateData.review}/review_update/`, reviewUpdateData, axiosConfig)
            .then((response) => {
              console.log(response)
              alert('지워드렸습니다^^')
              this.$router.push(`/boards/${reviewUpdateData.movie}/`)
            })
            .catch((error) => {
              console.log(error.response)
              alert(error[0])
            })
        } else {
          alert('먼저 로그인을 해주세요')
          
        }
      
    },
    search: function(){
      axios.post(`${BACK_URL}/boards/search/`, this.searchData)
        .then((response) => {
          this.searchResultData.movies = response.data[0]
          this.searchResultData.reviews = response.data[1]
          this.searchResultData.users = response.data[2]
          this.$router.push('/search/')
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error.response)
        })
    },
    changeColorR : function(){
      this.color = 1
    },
    changeColorP : function(){
      this.color = 2
    },
    changeColorM : function(){
      this.color = 3
    },
    changeColorY : function(){
      this.color = 4
    },
    myProfile: function () {
            this.$router.push(`/accounts/profile/${this.myInformation[0].id}`)
        },
    
   

  
  },
  computed: {
        
        
  },
  created: function () {
    this.isLoggedIn = this.$cookies.isKey('auth-token')
    this.getUser()
  },

}

</script>

<style>
a{
  text-decoration: none;
}
.f-b{
  font-size: 1.5rem;
}
.nav-pad{
  margin: auto;
}
.main-bar{
  margin-right: 150px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.searchbar{
    margin-bottom: auto;
    margin-top: auto;
    height: 50px;
    background-color: rgba(146, 143, 143, 0.5);
    border-radius: 30px;
    padding: 6px;
    }

.search_input{
    color: white;
    border: 0;
    outline: 0;
    background: none;
    width: 0;
    caret-color:transparent;
    line-height: 30px;
    transition: width 0.3s linear;
    }

.searchbar:hover > .search_input{
    padding: 0 10px;
    width: 200px;
    caret-color:red;
    transition: width 0.4s linear;
    }

.searchbar:hover > .search_icon{
    background: white;
    color: #e74c3c;
    }

.search_icon{
    height: 40px;
    width: 40px;
    float: right;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    color:white;
    text-decoration:none;
    }
.bg-violet{
  background-color: violet;
}
.bg-purple{
  background-color: purple;
}
.bg-yellow{
  background-color: #e0d900;
}
.bg-red{
  background-color:red;
}

</style>
