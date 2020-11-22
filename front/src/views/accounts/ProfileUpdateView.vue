<template>


    <div class="bgrand3">

<div class="page">
    <div style="height:10px;"></div>
    <div style="margin-top : 200px;"></div>
	<div class="display-table">
        <div class="coll">
			<div class="contact-info">
				<img src="../../assets/pngwingcom.png"  alt="image"/>
				<h4 style="font-family: 'Staatliches', cursive;">Profile Update</h4>
                <br>
				<h5 style="font-family: 'Jeju Gothic', sans-serif;">자유롭게 <br> 작성해 주세요!</h5>
			</div>
		</div>
		<div class="display-table-cell">

			<div class="container">
				<h3 style="font-family: 'Staatliches', cursive;"> 프로필 <span>수정</span></h3>

				<div class="contact">
					<div class="contact-box">

						<form id="contactForm" class="text-left form-group-lg" @submit="submitFile">

						<div class="form-group">
							<label for="contact_subject" style="font-family: 'Jeju Gothic', sans-serif;">프로필 사진 *</label>
							
                           <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
						</div>

						<div class="form-group">
							<label for="contact_message" style="font-family: 'Jeju Gothic', sans-serif;">One_thing *</label>
							<textarea class="form-control" id="contact_message" name="contact_message" rows="10" title="Message" v-model="profileUpdateData.one_thing"></textarea>
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
    name:'ProfileUpdateView',
    data: function () {
        return {
            profileUpdateData:{
                img:'',
                one_thing:''
            },
        }
    },
    props:{
        isLoggedIn: Boolean,
        myInformation:Array
    },
    methods: {
        
        
        submitFile: function (event) {
            event.preventDefault()
            console.log('test')
            if (this.isLoggedIn){
                const axiosConfig = {
                headers:{
                    Authorization: `Token ${this.$cookies.get('auth-token')}`,
                    'Content-Type': 'multipart/form-data'
                },
                }
                let formData = new FormData();

            /*
                Add the form data we need to submit
            */
                formData.append('img', this.profileUpdateData.img);
                formData.append('one_thing', this.profileUpdateData.one_thing);

            axios.post(`${BACK_URL}/boards/profile_update/${this.$route.params.userId}/`, formData, axiosConfig)
                .then((response) => {
                console.log(response)
                
                this.$router.push(`/accounts/profile/${this.$route.params.userId}/`)
                })
                .catch((error) => {
                console.log(error.response)
                alert('잘못된 시도입니다.')
                })
            } else {
                alert('먼저 로그인을 해주세요')
                
            }
            
           

        },
        changeColor:function(){
            this.$emit('change-color-M')
        },
        handleFileUpload(){
        this.profileUpdateData.img = this.$refs.file.files[0];
        }
    },

        

     
    mounted: function () {
        this.changeColor()
        
        
    },

}
</script>

<style>

</style>