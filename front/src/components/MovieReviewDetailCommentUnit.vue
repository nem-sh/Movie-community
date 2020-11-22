<template>
  <!-- <div style="color:white">
    <p>content : {{comment.content}}</p>
    <p>writer : {{comment.writer.username}}</p>
    <hr>
  </div> -->
  <div class="col-3">
      <div class="card border-warning ml-2 mr-2 mt-4" style="max-width: 18rem;">
  <div class="card-header" @click="goProfile">{{comment.writer.username}}</div>
  <div class="card-body text-warning">
    <p class="card-text">{{comment.content}}</p>
    <small>{{comment.created_at}}</small>
    <br>
    <button class="btn btn-danger" @click="commentDelete" v-if="myInformation[0].id == comment.writer.id">삭제</button>
  </div>
</div>

  </div>

</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'
export default {
    name: 'MovieReviewDetailCommentUnit',
    props:{
        comment: Object,
        myInformation : Object,
        isLoggedIn:Boolean
    },
    methods :{
      commentDelete: function () {
      
        if (this.isLoggedIn){
          const axiosConfig = {
            headers:{
              Authorization: `Token ${this.$cookies.get('auth-token')}`
            },
          }
          console.log('bi')
          axios.post(`${BACK_URL}/boards/${this.$route.params.movieId}/${this.$route.params.reviewId}/${this.comment.id}/comment_delete/`, this.comment, axiosConfig)
            .then(() => {
              this.$emit('delete-comment')
            })
            .catch((error) => {
              console.log(error.response)
              alert(error[0])
            })
        } else {
          alert('먼저 로그인을 해주세요')
          
        }
        },

      goProfile : function(){
          this.$router.push(`/accounts/profile/${this.comment.writer.id}`)
      }
    },
    created() {
          this.comment.created_at = this.comment.created_at.slice(0,10) +' '+this.comment.created_at.slice(11,19)
          this.comment.updated_at = this.comment.updated_at.slice(0,10) +' '+this.comment.updated_at.slice(11,19)
        
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
</style>