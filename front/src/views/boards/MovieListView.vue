<template>

    <!-- <div>
        
        <h1>MainList</h1>

        <div class="container">

            <div class="row">

                <MovieListUnit :key="movie.id" v-for="movie in movies" :movie="movie"/>

            </div>

        </div>

    </div> -->
    <div class="listView">
        
        <div class="bgbg">
            <br>
            <br><br>
            <br>

            
        <div id="carouselExampleCaptions" class=" d-flex carousel slide " data-ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
            <img src="http://artinsight.co.kr/data/tmp/1605/09fb2a5d50a8b05a0c7911d25a3e2f41_9EFhK16FshL5nAuwsA3zpRutu44ELVE9.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
                <h5 class="caption_title" style="font-family: 'Lobster', cursive;">ABOUT TIME</h5>
                <p class="caption_content">"We're all traveling through time together, 
                    every day of our lives All we can do is our best to relish this remarkable ride"</p>
            </div>
            </div>
            <div class="carousel-item">
            <img src="https://www.artinsight.co.kr/data/tmp/1906/daab7f300145a1c918987c841ca54c24_FYq1Iok5aO9gDh6bFCuV.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
                <h5 class="caption_title2" style="font-family: 'Lobster', cursive;" >BEGIN AGAIN</h5>
                <p class="caption_content2">"that's what I love about music, All these banalites suddenly turn into beautiful peals"</p>
            </div>
            </div>
            <div class="carousel-item">
            <img src="https://www.artinsight.co.kr/data/tmp/2003/20200306212607_hfkpydur.png" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
                <h5 class="caption_title3" style="font-family: 'Lobster', cursive;">LADY BIRD</h5>
                <p>Mom: "I want you to be the very best version of yourself that you can be"</p>
                <p>Bird: "What if this is the best version?"</p>
            </div>
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon"  aria-hidden="true"></span>
            <span class="sr-only" >Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
        </div>
        </div>
        <br>
        <hr align="center" style="border: solid 0.5px gray;  width: 80%;">
        <br>

        
        <div class="container" style="margin: auto;  " v-if="recommendMovies1">
            <div class="row" style="margin: auto; height:476px;">

            
            <div class=" col-2 rounded mx-auto card kk" style="background-color: black; height:576px; margin:auto;">
                <div class="card-body p-0">
                    <h4 class="card-title" style=" margin-top:250px;">Recommend</h4>
                    <h6 class="card-subtitle mb-2 text-muted">당신에 맞춘 영화</h6>
                </div>
            </div>
            <div id="carouselExampleInterval" class="carousel slide mr-0 col-10" data-ride="carousel" style="margin: auto; height:476px;">
            <div class="carousel-inner">
                <div class="carousel-item active" data-interval="10000" v-if="!isLoggedIn">
                    <h1 style="margin-top: 200px;">로그인하세요!</h1>
                </div>
                <div else class="carousel-item active" data-interval="10000">
                    
                    <MovieListUnit :movie="recommendMovies1[0]" v-if="recommendMovies1[0]"/>
                    
                    <h1 style="margin-top: 200px;" v-if="!recommendMovies1[0]">추천데이터가 부족합니다!</h1>
                    <MovieListUnit :movie="recommendMovies1[1]" v-if="recommendMovies1[1]"/>
                    <MovieListUnit :movie="recommendMovies1[2]" v-if="recommendMovies1[2]"/>
                </div>
                <div class="carousel-item" data-interval="10000" v-for="movies in recommendMovies" :key="movies[0]">
                    <MovieListUnit :movie="movies[0]" v-if="movies[0]"/>
                    <MovieListUnit :movie="movies[1]" v-if="movies[1]"/>
                    <MovieListUnit :movie="movies[2]" v-if="movies[2]"/>
                </div>
                
                
            </div>
            <a class="carousel-control-prev " href="#carouselExampleInterval" role="button" data-slide="prev" style="width:100px;">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next" style="width:100px;">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
            </div>
            </div>
        </div>
        
        <div class="container" style="margin: auto; height:476px;" v-if="recommendUser1">
            <div class="row" style="margin: auto; height:476px;">

            
            <div class=" col-2 rounded mx-auto card kk2" style="background-color: black; height:576px; margin:auto;">
                <div class="card-body p-0">
                    <h4 class="card-title" style=" margin-top:250px;">Movie mate</h4>
                    <h6 class="card-subtitle mb-2 text-muted">당신과 꼭 닮은 그들</h6>
                </div>
            </div>
            <div id="carouselExampleInterval" class="carousel slide mr-0 col-10" data-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active" data-interval="10000" v-if="!isLoggedIn">
                    <h1 style="margin-top: 200px;">로그인하세요!</h1>
                </div>
                <div else class="carousel-item active" data-interval="10000">
                    <MovieListUserUnit  :movie="recommendUser1[0]" v-if="recommendUser1[0]"/>
                    <h1 style="margin-top: 200px;" v-if="!recommendUser1[0]">추천데이터가 부족합니다!</h1>
                    <MovieListUserUnit  :movie="recommendUser1[1]" v-if="recommendUser1[1]"/>
                    <MovieListUserUnit  :movie="recommendUser1[2]" v-if="recommendUser1[2]"/>
                </div>
                <div class="carousel-item" data-interval="10000" v-for="users in recommendUser" :key="users[0]">
                    <MovieListUserUnit :movie="users[0]" v-if="users[0]"/>
                    <MovieListUserUnit :movie="users[1]" v-if="users[1]"/>
                    <MovieListUserUnit :movie="users[2]" v-if="users[2]"/>
                </div>
                
                
           </div>
            <a class="carousel-control-prev " href="#carouselExampleInterval" role="button" data-slide="prev" style="width:100px;">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-slide="next" style="width:100px;">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
            </div>
        </div>
        </div>
        
        <hr>

        <div class="container">

            <div class="row">

                <MovieListUnit :key="movie.id" v-for="movie in movies" :movie="movie"/>
            </div>
        </div>
    
    <br><br><br><br><br>
    </div>  

</template>

<script>
import MovieListUnit from '../../components/MovieListUnit.vue'
import MovieListUserUnit from '../../components/MovieListUserUnit.vue'


import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'


export default {

    name:'MovieListView',
    components: {
        MovieListUnit,
        MovieListUserUnit,
    },
    data() {
        return {
        movies: null,
        recommendMovies: null,
        recommendUser: null,
        recommendMovies1: null,
        recommendUser1: null,

        }
    },
    props : {
        isLoggedIn : Boolean,
    },
    methods: {

        getMovies() {
            let axiosConfig = null
            if (this.isLoggedIn){
                axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
                }
            
            }
            axios.post(`${BACK_URL}/boards/`,null,axiosConfig)
                .then((response) => {
                    console.log(response)
                    
                    this.movies = response.data[0]
                    this.recommendMovies1 = this.function1(response.data[2],3)[0]
                    this.recommendUser1 = this.function1(response.data[1],3)[0]
                    this.recommendMovies = this.function2(response.data[2],3)
                    this.recommendUser = this.function2(response.data[1],3)
            })
        },
        function1 (arr1, n) {
            
            var tmp = [];
            tmp.push(arr1.splice(0, n));

            return tmp;
        },

        function2 (arr1, n) {
            var len = arr1.length-1;
            var cnt = Math.floor(len / n);
            var tmp = [];
            // var a = []
            // a.push(arr1.splice(0,n))
            for (var i = 0; i < cnt; i++) {
                tmp.push(arr1.splice(0, n));
            }

            return tmp;
        },
        changeColor (){
            this.$emit('change-color-R')
        },
        
    },

    created() {
        this.getMovies();
        
        this.changeColor()
        ;
    }


}


</script>

<style>
    .listView{
        background-color: black;
    }
    .bgbg{
         background: -webkit-linear-gradient(90deg, black 50%, red 20%);

    }

    .carousel{
        margin: auto;
        width: 1000px;
        height: 400px;
        

    }

    .carousel .item, .carousel .item.active, .carousel .carousel-inner {

        margin: auto;
        width: 75%;
        height: 100%;
        border-radius: 20px;

    }

    .carousel .fill {

        width: 100%;

        height: 100%;

        background-position: center;

        background-size: auto 100%;

    }
    .carousel-indicators{
        margin-bottom: -30px;
    }
    .carousel-control-prev-icon, .carousel-control-next-icon {
        height: 50px;
        width: 50px;
        outline: black;
        background-size: 50%, 50%;
        border-radius: 50%;
        border: 1px solid white;
        filter: invert(0%);
    }
    img{
        height: 400px;
    }
    .caption_title {
    
        color: red !important;
        width: 300px;
        margin-bottom: 10px;
        font-size: 3rem;

    }
    .caption_content{
        color: white;
        margin-bottom: 60px;
        width: 200px;
        margin-left: 40px;
        
    }
    .caption_title2 {
    
        color: yellow !important;
        width: 300px;
        padding-right: 300px;
        margin-right: 300px;
        margin-bottom: 100px;
        font-size: 3rem;

    }
    .div, .caption_content2{
        color: white;
        text-align: right;
        padding-left: 200px;
        
    }
    .caption_title3 {
    
        color: hotpink !important;
        margin-bottom: 200px;
        font-size: 3rem;
    }
    .kk:hover {
        color: hotpink;
    }
    .kk2:hover {
        color: red;
    }





</style>