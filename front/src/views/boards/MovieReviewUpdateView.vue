<template>
    <!-- <div>
        <h1>Review Update</h1>

        <form @submit="reviewUpdate">

            <div class="form-group">
                <label for="title">Title</label>
                <input id="title" type="text" class="form-control"  aria-describedby="titleHelp" placeholder="제목 적어라" v-model="reviewUpdateData.title">
                <small id="titleHelp" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요.</small>
            </div>

            <div class="form-group">
                <label for="content">Content</label>
                <input id="content" type="text" class="form-control"  placeholder="내용 적어라" v-model="reviewUpdateData.content">
            </div>

            <button class="btn btn-primary">Submit</button>

        </form>
  </div> -->

    <div class="bgrand3">

<div class="page">
    <div style="height:10px;"></div>
    <div style="margin-top : 200px;"></div>
	<div class="display-table">
        <div class="coll">
			<div class="contact-info">
				<img src="../../assets/pngwingcom.png"  alt="image"/>
				<h4 style="font-family: 'Staatliches', cursive;">Movie Review</h4>
                <br>
				<h5 style="font-family: 'Jeju Gothic', sans-serif;">자유롭게 <br> 작성해 주세요!</h5>
			</div>
		</div>
		<div class="display-table-cell">

			<div class="container">
				<h3 style="font-family: 'Staatliches', cursive;"> MOVIE <span>REVIEW</span></h3>

				<div class="contact">
					<div class="contact-box">

						<form id="contactForm" class="text-left form-group-lg" @submit="reviewUpdate">

						<div class="form-group">
							<label for="contact_subject" style="font-family: 'Jeju Gothic', sans-serif;">제목 *</label>
							<input type="text" class="form-control" id="contact_subject" name="contact_subject" title="Subject" v-model="reviewUpdateData.title">
						</div>

						<div class="form-group">
							<label for="contact_message" style="font-family: 'Jeju Gothic', sans-serif;">내용 *</label>
							<textarea class="form-control" id="contact_message" name="contact_message" rows="10" title="Message" v-model="reviewUpdateData.content"></textarea>
						</div>

						<div class="form-group text-center">
							<button id="contact_submit"  class="btn btn-primary1" style="font-family: 'Staatliches', cursive;">COMPLETE</button>
						</div>

						</form>

					</div>
				</div>

			</div>

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
</div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'
export default {
    name:'MovieReviewUpdateView',
    data: function () {
        return {
            reviewUpdateData:{
                title:'',
                content:'',
                movie: this.$route.params.movieId,
            },
            review: null
        }
    },
    props:{
        isLoggedIn: Boolean,
    },
    methods: {
        getUpdateData: function () {
            
            axios.get(`${BACK_URL}/boards/${this.$route.params.movieId}/${this.$route.params.reviewId}/review_detail/`)
                .then((response) => {
                    console.log(response)
                    this.review = response.data[0]
                    this.reviewUpdateData.title = this.review.title
                    this.reviewUpdateData.content = this.review.content
                    
            })
        },
        
        reviewUpdate: function () {

            if (this.isLoggedIn){
                const axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                },
            }
            axios.post(`${BACK_URL}/boards/${this.$route.params.movieId}/${this.$route.params.reviewId}/review_update/`, this.reviewUpdateData, axiosConfig)
                .then((response) => {
                console.log(response)
                
                alert('작성완료')
                })
                .catch((error) => {
                console.log(error.response)
                alert('잘못된 시도입니다.')
                })
                 this.$router.push(`/boards/${this.$route.params.movieId}/${this.$route.params.reviewId}/`)
            } else {
                alert('먼저 로그인을 해주세요')
                
            }
            
           

        },
        changeColor:function(){
            this.$emit('change-color-M')
        },
    },

        

     
    mounted: function () {
        this.getUpdateData()
        this.changeColor()
        
        
    },

}
</script>

<style>

</style>