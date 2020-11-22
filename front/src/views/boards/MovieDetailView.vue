<template>

    <div class="bgrand" style="background-color :black; color: white;">

   <div class="container" v-if="movie">
    <div style="height:10px;"></div>
    <div style="margin-top : 200px;"></div>

    <h5 class="display-4 " style="text-align : left;">{{movie.title}}</h5>
    <hr align="center" style="border: solid 0.5px purple;  width: 100%;">
    <div class="container">
        <div class="row">
            <img :src="getPosterPath" alt="" class="col-3">
            <div class="col-9" style="height:400px">
                <p style="text-align : left;">원제 : {{movie.original_title}}</p>
                
                <p style="text-align : left;">개봉일 : {{movie.release_date}}</p>
                
                <p style="text-align : left;">제작 국가 :{{movie.original_language}}</p>
                
                <p style="text-align : left;">장르 : <span v-for="genre in movie.genres" :key="genre.name"> {{genre.name}}</span>
                <p class="skip ">{{movie.overview}}</p>
                <br>
                <div style="text-align : left;">
                    <i class="fas fa-star display-4" v-if="like[0].score>0" style="color :yellow;" @click="one"></i>
                <i class="fas fa-star display-4" v-else @click="one"></i> 
                <i class="fas fa-star display-4" v-if="like[0].score > 1" @click="two" style="color :yellow;"></i>
                <i class="fas fa-star display-4" v-else @click="two"></i>
                <i class="fas fa-star display-4" v-if="like[0].score > 2" @click="three" style="color :yellow;"></i>
                <i class="fas fa-star display-4" v-else  @click="three"></i>
                <i class="fas fa-star display-4" v-if="like[0].score > 3" @click="four" style="color :yellow;"></i>
                <i class="fas fa-star display-4" v-else @click="four"></i>
                <i class="fas fa-star display-4" v-if="like[0].score > 4" @click="five" style="color :yellow;"></i>
                <i class="fas fa-star display-4" v-else @click="five"></i>
                <router-link class="btn btn-primary btn-lg"  style="margin-left:250px; background-color : purple; border:0px" :to="enterMovieReviewCreate" tag="button">Write review now!</router-link>
                </div>
                <p style="text-align : left; color:red; font-weight: bold;" v-if="like[0].score==0">평점을 매겨주세요.</p>
                

            </div>
        </div>

            
      
    </div>

    <br>
    <hr align="center" style="border: solid 0.5px purple;  width: 100%;">
    <br>


        <table class="table">
        <thead class="thead-light">
            <tr>
            <th scope="col">#</th>
            <th scope="col">title</th>
            <th scope="col">writer</th>
            </tr>
        </thead>
        <tbody>
            <MovieReviewListUnit :key="review.id" v-for="review in reviews" :review="review"/>
    
            
        </tbody>
    </table>
    
        <h1 v-if="!reviews[0]" style="margin-top:100px;margin-left:200px;">첫 리뷰의 주인공이 되세요!</h1>

    </div>
    
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
</div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'


import MovieReviewListUnit from '../../components/MovieReviewListUnit'

export default {
    name: 'MovieDetailView',
    components:{
        MovieReviewListUnit,
    },
    data () {
        return{
            movie: null,
            reviews: null,
            like: null,
            movieLikeData:{
                score:0,
                movie: this.$route.params.movieId,
            },
        }
    },

    props : {
        isLoggedIn : Boolean,
    },
    computed: {

        param: function () {
            return this.$route.params;
        },

        enterMovieReviewCreate: function () {
            return `/boards/${this.$route.params.movieId}/review_create`
        },
        getPosterPath: function () {
            return `https://image.tmdb.org/t/p/w154/${this.movie.poster_path}`
        },
        
    },


    methods: {
        getMovieDetail() {
            let axiosConfig = null
            if (this.isLoggedIn){
                axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
                }
            
            }
            
            axios.post(`${BACK_URL}/boards/${this.$route.params.movieId}/`,null,axiosConfig)
            .then((response) => {
                console.log(response)
                this.movie = response.data[0]
                this.reviews = response.data[1]
                this.like = response.data[2]

            })
        },


        movieLike: function () {
            
            if (this.isLoggedIn){
                const axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
                }
            axios.post(`${BACK_URL}/boards/${this.movieLikeData.movie}/likelike/`, this.movieLikeData, axiosConfig)
                .then((response) => {
                console.log(response)
                this.like[0].score = this.movieLikeData.score
                })
                .catch((error) => {
                console.log(error.response)
                alert('다시 작성하도록!')
                })
            } else {
                alert('먼저 로그인을 해주세요')
                
            }

        
        },
        one:function(){
            this.movieLikeData.score = 1
            this.movieLike()
        },
        two:function(){
            this.movieLikeData.score = 2
            this.movieLike()
        },
        three:function(){
            this.movieLikeData.score = 3
            this.movieLike()
        },
        four:function(){
            this.movieLikeData.score = 4
            this.movieLike()
        },
        five:function(){
            this.movieLikeData.score = 5
            this.movieLike()
        },

        changeColor:function(){
            this.$emit('change-color-P')
        }
    },
    

    


    created() {
        this.getMovieDetail()
        this.changeColor()
    },


}
</script>

<style>
.skip {
  overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 6; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 7.2em; /* line-height 가 1.2em 이고 3라인을 자르기 때문에 height는 1.2em * 3 = 3.6em */
    
    text-align : left;

    
  }
    .bgbg1{
    background: -webkit-linear-gradient(90deg, black 50%, violet 20%);

}
</style>