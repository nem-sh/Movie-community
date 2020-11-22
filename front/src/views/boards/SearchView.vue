<template>
  
  <div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>


    <nav aria-label="...">

      <ul class="pagination pagination-lg">
        <li :class="{active: page==1}" class="page-item" @click="changePage1"><a class="page-link" href="#">Movie</a></li>
        <li :class="{active: page==2}" class="page-item" @click="changePage2"><a class="page-link" href="#">Review</a></li>
        <li :class="{active: page==3}" class="page-item" @click="changePage3"><a class="page-link" href="#">User</a></li>
      </ul>
    </nav>
    <div v-if="page==1">
      <h5 class="display-4 " style="width: 35%; margin-right:0;">Movie 결과</h5>
      <hr align="center" style="border: solid 0.5px purple;  width: 80%;">
      <div class="container">

              <div class="row">

                  <MovieListUnit :key="movie.id" v-for="movie in searchResultData.movies" :movie="movie"/>
              </div>
              <h1 v-if="!searchResultData.movies[0]" style="margin-top:100px;margin-left:200px;">검색결과가 없습니다.</h1>
      </div>
    </div>

    <div v-if="page==2">
      <h5 class="display-4 " style="width: 35%; margin-right:0;">Review 결과</h5>
      <hr align="center" style="border: solid 0.5px purple;  width: 80%;">
        <table class="table" style="width:60%; margin:0 auto;">
        <thead class="thead-light">
            <tr>
            <th scope="col">#</th>
            <th scope="col">title</th>
            
            <th scope="col">movie</th>
            <th scope="col">writer</th>
            </tr>
        </thead>
        <tbody>
            <CommunityUnit :key="review.id" v-for="review in searchResultData.reviews" :review="review"/>
    
        </tbody>    
        
            
        </table>
        <h1 v-if="!searchResultData.reviews[0]" style="margin-top:100px;margin-left:200px;">검색결과가 없습니다.</h1>
    </div>

    <div v-if="page==3">
      <h5 class="display-4 " style="width: 35%; margin-right:0;">User 결과</h5>
      <hr align="center" style="border: solid 0.5px purple;  width: 80%;">
    <div class="container">

            <div class="row">

                <MovieListUserUnit :key="movie.id" v-for="movie in searchResultData.users" :movie="movie"/>
            </div>
    </div>
    
              <h1 v-if="!searchResultData.users[0]" style="margin-top:100px;margin-left:200px;">검색결과가 없습니다.</h1>
    </div>
    
  </div>
</template>

<script>
import MovieListUnit from '../../components/MovieListUnit.vue'
import CommunityUnit from '../../components/CommunityUnit.vue'

import MovieListUserUnit from '../../components/MovieListUserUnit.vue'
export default {
    name:'SearchView',
    data(){
      return{
        page: 1,
      }
    },
    components: {
        MovieListUnit,
        MovieListUserUnit,
        CommunityUnit,
    },
    props:{
        searchResultData: Object,
    },
    methods:{
      changePage1(){
        this.page =1
      },
      changePage2(){
        this.page =2
      },
      changePage3(){
        this.page =3
      }
    }
}
</script>
    
<style>

</style>