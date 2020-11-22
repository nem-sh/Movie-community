<template>
    <!-- <div>
        <div v-if="review">
        parameter : {{param}}
        <br/>
        {{review.title}}의 detail
        <br/>
        {{review.content}}
        <br/>
        <button class="btn btn-primary" @click="movieReviewDelete">Delete review</button>
        
        
        <router-link class="btn btn-primary" :to="movieUpdate" tag="button">update</router-link>
        <br/>
        <h1>Comment Create</h1>

        <form @submit="reviewCommentCreate">

            <div class="form-group">
                <label for="content">Content</label>
                <input id="content" type="text" class="form-control"  aria-describedby="titleHelp" placeholder="제목 적어라" v-model="reviewCommentCreateData.content">
                <small id="contentHelp" class="form-text text-muted">리뷰와 관련된 자유로운 의견을 남겨주세요.</small>
            </div>

            <button class="btn btn-primary">Submit</button>

        </form>

        <MovieReviewDetailCommentUnit :key="comment.id" v-for="comment in comments" :comment="comment"/>
        </div>
    </div> -->


    
<div class="bgrand3">
<div class="page" v-if="review">
    <div style="height:10px;"></div>
    <div style="margin-top : 200px;"></div>
	<div class="display-table">
        <div class="coll2">
			<div class="contact-info">
				<img src="../../assets/movie.png"  alt="image"/>
				<h4 style="font-family: 'Staatliches', cursive;">Movie Detail</h4>
                <br>
				<h5 style="font-family: 'Jeju Gothic', sans-serif;">댓글 <br> 작성해 주세요!</h5>
			</div>
		</div>
		<div class="display-table-cell">

			<div class="container">
				<h3 class="label-detail" style="font-family: 'Staatliches', cursive;"> MOVIE <span style="color: #dfbc23; ">DETAIL</span></h3>

				<div class="contact">
					<div class="contact-box">

						<form id="contactForm"    class="text-left form-group-lg">

						<div class="form-group">
							<label class="label-detail" for="contact_subject" style="font-family: 'Jeju Gothic', sans-serif;">제목 :{{review.title}}</label>
						</div>
                        <div class="form-group">
							<label class="label-detail" for="contact_subject" style="font-family: 'Jeju Gothic', sans-serif;">작성일/수정일 :{{review.created_at}} / {{review.updated_at}}</label>
						</div>

						<div class="form-group">
							<label class="label-detail" for="contact_message" style="font-family: 'Jeju Gothic', sans-serif;">내용 :{{review.content}}</label>

						</div>
                        <div style="margin-left:250px;" v-if="isWriter">
                            <router-link class="btn btn-info mr-3" :to="movieUpdate" tag="button">Update</router-link>
                            <button class="btn btn-danger" @click="movieReviewDelete">Delete</button>
                        </div>
                        
		
                        
                        
                        
           

						</form>
                        <form  @submit="reviewCommentCreate">
                            <div class="form-group">
                            <label class="label-detail" for="comment">Your Comment</label>
                            <textarea name="comment" class="form-control" rows="3" v-model="reviewCommentCreateData.content"></textarea>
                        </div>
                        
                        <button  class="btn btn-primary2">Send</button>
                        </form>
                        
            
                        

					</div>
				</div>
    
			</div>

		</div>
        
	</div>
    
    <hr align="center" style="border: solid 0.5px yellow;  width: 75%;">
    <div class="continer" style="width:800px; margin: auto;">
        <div class="row">
            <MovieReviewDetailCommentUnit :key="comment.id" v-for="comment in comments" :comment="comment" :myInformation="myInformation" :isLoggedIn="isLoggedIn" @delete-comment="deleteComment"/>
        </div>
    </div>

    
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
</div>

</template>

<script>
import MovieReviewDetailCommentUnit from '../../components/MovieReviewDetailCommentUnit'

import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    name : 'MovieReviewDetailView',

    components:{
        MovieReviewDetailCommentUnit,
    },

    data () {
        return{
            review: null,
            comments: null,
            reviewDeleteData: {
                movie : this.$route.params.movieId,
                review: this.$route.params.reviewId,
            },
            reviewCommentCreateData:{
                content:'',
                movie: this.$route.params.movieId,
                review: this.$route.params.reviewId,
            },
            isWriter: false
        }
    },
    props : {
        isLoggedIn : Boolean,
        myInformation : Object
    },

    computed: {

        param: function () {
            return this.$route.params;
        },
        movieUpdate: function () {
            return `/boards/${this.$route.params.movieId}/${this.$route.params.reviewId}/review_update/`
        },

        

    },

    methods: {
        getMovieReviewDetail() {
            let axiosConfig = null
            if (this.isLoggedIn){
                axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
                }
            }
            axios.post(`${BACK_URL}/boards/${this.$route.params.movieId}/${this.$route.params.reviewId}/review_detail/`,null ,axiosConfig)
            .then((response) => {
                console.log(response)
                this.review = response.data[0]
                this.comments = response.data[1]
                this.isWriter = response.data[2].isWriter
                this.review.created_at = response.data[0].created_at.slice(0,10) +' '+response.data[0].created_at.slice(11,19)
                this.review.updated_at = response.data[0].updated_at.slice(0,10) +' '+response.data[0].updated_at.slice(11,19)
                

            })

        },
        movieReviewDelete() {
            console.log('hi')
            this.$emit('submit-review-delete-data', this.reviewDeleteData)

            
        },

        reviewCommentCreate: function (event) {
            event.preventDefault()
            
            console.log(this.reviewCommentCreateData)
            if (this.isLoggedIn){
                const axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
                }
            console.log(this.reviewCommentCreateData)
            axios.post(`${BACK_URL}/boards/${this.reviewCommentCreateData.movie}/${this.reviewCommentCreateData.review}/comment_create/`, this.reviewCommentCreateData, axiosConfig)
                .then((response) => {
                console.log(response)
                alert('작성했습니다^^')
                this.getMovieReviewDetail()
                })
                .catch((error) => {
                console.log(error.response)
                alert('다시 작성하도록!')
                })
            } else {
                alert('먼저 로그인을 해주세요')
                
            }
            
            
        },
        changeColor : function(){
            this.$emit('change-color-y')
        },
        deleteComment:function(){
            
            this.getMovieReviewDetail()
        }


            
    },

        

         


    


    created() {
        this.getMovieReviewDetail()
        this.changeColor()
    },


}
</script>


<style>
.bgrand3{
    background-color: black;
}

.coll2{
    background: #dfbc23;
    padding: 4%;
    border-top-left-radius: 0.5rem;
    border-bottom-left-radius: 0.5rem;
    margin-right: 0 !important;
    margin-left: 250px;
    height: 80%;
    width: 200px;
}
.contact-info{
    margin-top:10%;
    width: 10rem;
}
.contact-info img{
    margin-bottom: 15%;
    width: 4rem;
    height: 4rem;
}
.contact-info h2{
    margin-bottom: 10%;
}
div.page {

	left:0; right:0;
	top:0; bottom:0;
	z-index:9;
	text-align:center;
}
div.page .container {
	padding-bottom:100px;
}
div.page h3 {
	font-family: "Roboto", sans-serif;
	font-size:35px;
	margin-bottom:20px;
	font-weight:300;
    color: white;
    text-align: center;
    margin-right: 20rem;
}
div.page p {
	margin-bottom:40px;
}

.display-table {
	display:table;
	width:100%;
	height:100%;
}
.display-table-cell {
	display:table-cell;
	vertical-align:middle;
	width:100%;
	height:100%;
}





/* form styling */
.label-detail {
	font-weight:400;
	text-transform:uppercase;
	font-size:15px;
    color: #dfbc23;
}
button::-moz-focus-inner, 
input::-moz-focus-inner {
	border: 0;
	padding: 0;
}
textarea, input, button, *:focus {
	outline:none !important;
}
textarea {
	resize: vertical;
    
}


.btn-primary2 {
	border-color:#dfbc23 !important;
	background-color:#dfbc23;
    width: 200px;
    height: 50px;

}
.contact-box{
    margin-right: 300px;
}


</style>