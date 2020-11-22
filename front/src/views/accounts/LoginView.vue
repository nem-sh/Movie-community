<template>
    <!-- <div>
        <br>
        <br>
        <h1>로그인</h1>
        username: <input type="text" v-model="loginData.username"/>
        <hr/>
        password: <input type="password" v-model="loginData.password"/>
        <hr/>
        <button @click="login">로그인</button>
    </div> -->

     <div class="back">
    <div class="container">
        <div style="height:10px;"></div>
        <div style="margin-top : 200px;">
        <h3 style="text-align:left; font-family: 'Jeju Gothic', sans-serif;" class="text-white" >로그인</h3>
        <hr style="border: solid 0.5px gray;  width: 100%;">
        <br>
            <form @click="login" style="margin-right: 400px; margin-left:350px;">
                <div class="form-group" >
                    <input v-model="loginData.username" type="text" style="width:400px; height:70px; border-radius:30px; background-color: black; border: 0px;" class="form-control" id="InputId1" aria-describedby="emailHelp" placeholder="아이디">
                    <!-- <button class="close-icon" type="reset"></button> -->
                </div>
                <div class="form-group">
                    <input v-model="loginData.password" type="password" style="width:400px; height:70px; border-radius:30px;background-color: black; border: 0px;" class="form-control" id="InputPassword1" placeholder="비밀번호">
                </div>
                <button  style="width:400px; height:70px; border-radius:30px; font-family: 'Jeju Gothic', sans-serif;" class="btn btn-danger">로그인</button>
            </form>
        </div>
        
        <div style="height:350px;"></div>
    </div>
    
 </div>
</template>

<script>
export default {
    name:'LoginView',
    data: function  () {
        return {
            loginData : {
                    username:'',
                    password:'',
                
            },
        }
    },
    methods: {
        login: function (event) {
            
            event.preventDefault()
            this.$emit('submit-login-data', this.loginData)
        },
    },
}
</script>

<style>
.back{
    background-color: #313131;
}
</style>