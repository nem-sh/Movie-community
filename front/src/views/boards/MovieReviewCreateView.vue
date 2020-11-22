<template>
    <!-- <div>
        <h1>Review Create</h1>

        <form @submit="reviewCreate">

            <div class="form-group">
                <label for="title">Title</label>
                <input id="title" type="text" class="form-control"  aria-describedby="titleHelp" placeholder="제목 적어라" v-model="reviewCreateData.title">
                <small id="titleHelp" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요.</small>
            </div>

            <div class="form-group">
                <label for="content">Content</label>
                <input id="content" type="text" class="form-control"  placeholder="내용 적어라" v-model="reviewCreateData.content">
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

						<form id="contactForm" class="text-left form-group-lg" @submit="reviewCreate">

						<div class="form-group">
							<label for="contact_subject" style="font-family: 'Jeju Gothic', sans-serif;">제목 *</label>
							<input type="text" class="form-control" id="contact_subject" name="contact_subject" title="Subject" v-model="reviewCreateData.title">
						</div>

						<div class="form-group">
							<label for="contact_message" style="font-family: 'Jeju Gothic', sans-serif;">내용 *</label>
							<textarea class="form-control" id="contact_message" name="contact_message" rows="10" title="Message" v-model="reviewCreateData.content"></textarea>
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
export default {
    name:'MovieReviewCreateView',
    data: function () {
        return {
            reviewCreateData:{
                title:'',
                content:'',
                movie: this.$route.params.movieId,
            },
        }
    },
    methods: {
        reviewCreate: function (event) {
            event.preventDefault()
            console.log('test')
            this.$emit('submit-review-create-data', this.reviewCreateData)
		},
		changeColor:function(){
            this.$emit('change-color-M')
        },
	},
	mounted: function () {
        this.changeColor()
        
        
    },
}
</script>

<style>
.bgrand3{
    background-color: black;
}

.coll{
    background: #1EB7B1;
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
div.page h3>span {
	color:#1EB7B1;
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
label {
	font-weight:400;
	text-transform:uppercase;
	font-size:15px;
    color: #1b9e98;
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



input:focus {
	border-color:#1b9e98 !important;
}


.btn-primary1 {
	border-color:#1b9e98 !important;
	background-color:#1EB7B1;
    width: 200px;
    height: 50px;

}

.btn-primary1:active {
	border-color:#1b9e98 !important;
	background-color:#1b9e98;
}

.contact-box{
    margin-right: 300px;
}

</style>