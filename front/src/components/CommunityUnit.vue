<template>
    <tr style="color:white;">
        <th scope="row">{{review.id}}</th>
        <td><router-link :to="enterMovieReviewDetail" >{{review.title}}</router-link>
          </td>
          <td>{{review.movie.title}}</td>
        <td>{{review.writer.username}}</td>
    </tr>

</template>

<script>
export default {
    name:'CommunityUnit',

    props:{
        review: Object,
    },

    computed: {
        
        enterMovieReviewDetail: function () {
            return `/boards/${this.review.movie.id}/${this.review.id}`
        },
    },
}
</script>

<style>
.skip {
  overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 3.6em; /* line-height 가 1.2em 이고 3라인을 자르기 때문에 height는 1.2em * 3 = 3.6em */
    
    

    
  }
</style>