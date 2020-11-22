<template>
  <!-- <div>
      <h1>회원 가입</h1>
      username: <input type="text" v-model="signupData.username"/>
      <br/>
      password: <input type="password" v-model="signupData.password1">
      <br>
      password확인: <input type="password" v-model="signupData.password2"/>
      <br>
      <button @click="signup">회원가입</button>
  </div> -->

  <div class="back">
    <div class="container">
        <div style="height:10px;"></div>
        <div style="margin-top : 200px;">
        <h3 style="text-align:left; font-family: 'Jeju Gothic', sans-serif;" class="text-white" >회원가입</h3>
        <hr style="border: solid 0.5px gray;  width: 100%;">
        <br>
        <div   style="margin-right: 400px; margin-left:350px;">
            <div class="form-group">
                <input v-model="signupData.name" type="text" style="width:400px; height:60px; background-color: black; border: 0px; border-radius:10px;" class="form-control" id="Inputname" aria-describedby="nameHelp" placeholder="이름을 입력하세요.">
            </div>
            <div class="form-group">
                <input v-model="signupData.username" type="text" style="width:400px; height:60px; background-color: black; border: 0px; border-radius:10px;" class="form-control" id="InputID1" placeholder="아이디를 입력해 주세요.">
                <small id="namelHelp" class="form-text text-muted" style="text-align:left;"> ⓘ 6~12자 영문, 숫자를 입력해주세요.</small>
            </div>
            <br>
            <div class="form-group">
                <input v-model="signupData.password1" type="password" style="width:400px; height:60px; background-color: black; border: 0px; border-radius:10px;" class="form-control mb-1" id="InputPassword1" placeholder=" 8~20자의 영문,숫자를 조합하여 입력해주세요.">
                <input  v-model="signupData.password2" type="password" style="width:400px; height:60px; background-color: black; border: 0px; border-radius:10px;" class="form-control" id="InputPassword2" placeholder=" 비밀번호를 동일하게 한번 더 입력해주세요.">
                <small id="namelHelp" class="form-text text-muted"> ⓘ 비밀번호는 8~20자의 영문,숫자를 조합하여 입력해주세요.</small>
            </div>
                <button  @click="signup" style="width:400px; height:70px; border-radius:30px; font-family: 'Jeju Gothic', sans-serif;" class="btn btn-primary mt-2">회원가입</button>
        </div>

    </div>
    <div style="height:300px;"></div>
  </div>
</div>
</template>

<script>


export default {
    name:'SignupView',
    data: function () {
        return {
            signupData:{
                name:'',
                username:'',
                password1:'',
                password2:'',
            },
        }
    },

    methods: {


        signup: function (event) {
            
            event.preventDefault()
            this.$emit('submit-signup-data',this.signupData)
        },

    },

}
</script>

<style>

</style>