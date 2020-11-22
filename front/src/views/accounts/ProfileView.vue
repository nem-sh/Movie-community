<template>
  <div class="container" v-if="profileData">
      
  <br>
  <br>
  <br>
  <br>
  <br>
      <div class="card mb-3" style="max-width: 540px; margin-top: 100px;  ">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img v-if="profileData[0].img" :src="getImg" class="card-img" alt="" style="height:180px;">
      
      <img v-if="!profileData[0].img " src="../../assets/user_basic.jpg" class="card-img" alt="" style="height:180px;">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">{{profileData[0].username}}</h5>
        <p class="card-text"></p>
        <p class="card-text" style="height:100px;"><small class="text-muted">{{profileData[0].one_thing}}</small></p>
        <button class="btn btn-danger" @click="updateProfile" v-if="profileData[0].id == myInformation[0].id">프로필 수정</button>
      </div>
    </div>
    
  </div>
  
</div>
<br>
    <hr align="center" style="border: solid 0.5px purple;  width: 100%;">
    <h1 style="margin-right: 700px">{{profileData[0].username}}의 Favorite</h1>
    <div class="container">

            <div class="row">

                <MovieListUnit :key="movie.movie.id" v-for="movie in profileData[1]" :movie="movie.movie"/>
            </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import MovieListUnit from '../../components/MovieListUnit.vue'
const BACK_URL = 'http://127.0.0.1:8000'
export default {
    name:'ProfileView',
    components: {
        MovieListUnit,
       },
    data(){
        return{
            profileData :null
        }
    },
    props:{
        myInformation : Object
    },
    methods:{
        getUser() {

     
            
                axios.get(`${BACK_URL}/boards/profile/${this.$route.params.userId}/`)
                .then((response) => {
                    console.log(response)
                    console.log(response)
                    
                    console.log(111)
                    this.profileData = response.data

                })

            },

          updateProfile(){
            this.$router.push(`/accounts/profile_update/${this.$route.params.userId}/`)
          }

        },
    

   created() {
        this.getUser();
    },
    computed: {
        getImg: function () {
            return `${BACK_URL}${this.profileData[0].img}`
        },
        
    },
}
</script>

<style>
h1:hover{
    color:red;
}
</style>