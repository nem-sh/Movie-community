<template>
  <div style="margin-bottom:1000px; height : 5000px; background-color :black;"  >
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>

    <nav aria-label="...">

      <ul class="pagination pagination">
        <li  class="page-item" @click="genreName = genre.name" v-for="genre in movieData[0]" :key="genre.name" ><a class="page-link" href="#">{{genre.name}}</a></li>
      </ul >
      
    <hr align="center" style="border: solid 0.5px red;  width: 90%;">
      <div v-for="movieSet in movieData[0]" :key="movieSet.name">
            <div class="container" v-if="genreName== movieSet.name">
                <h1>{{genreName}}</h1>
            <div class="row">
                <h1 v-if="!movieSet.movie[0]" style="margin-top:100px ;color:red;"> 해당 장르 영화가 없습니다.</h1>
                <MovieListUnit :key="movieUnit.title" v-for="movieUnit in movieSet.movie" :movie="movieUnit"/>
            </div>
        </div>
      </div>
    </nav>

    <br>

  </div >
</template>

<script>
import MovieListUnit from '../../components/MovieListUnit.vue'
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    name:'MovieView',
    data(){
        return {
            movieData : null,
            genreName: null
        }
    },
    components: {
        MovieListUnit,
    },
    methods:{
            getMovie: function(){
                axios.get(`${BACK_URL}/boards/movie_genre/`)
                    .then((response) => {
                        this.movieData = response.data
                    
                    console.log(response.data)
                    })
                    .catch((error) => {
                    console.log(error.response)
                    })
                },
            
        changeColor (){
            this.$emit('change-color-R')
        },        
    },


    created(){
        
        this.changeColor()
        this.getMovie()
        
    }

}
</script>

<style>

</style>