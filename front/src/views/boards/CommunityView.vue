<template>
  <div style="background-color:black; ">
      <br><br><br><br><br><br>
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
            <CommunityUnit :key="review.id" v-for="review in reviews" :review="review"/>
    
            
        </tbody>    
        </table>
      

        <br><br><br><br><br><br>
  </div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'
import CommunityUnit from '../../components/CommunityUnit'
export default {
    name:'CommuityView',
    components:{
        CommunityUnit,
        
    },
    data(){
        return{
            reviews:null
        }
    },
    methods: {

        getReview() {
            
            axios.get(`${BACK_URL}/boards/reviews`)
                .then((response) => {
                    console.log(response)
                    
                    this.reviews = response.data
                    
            })
        },
    },
     created() {
        this.getReview();
        
    }
}
</script>

<style>
.bgbg1{
        background: -webkit-linear-gradient(90deg, black 59%, #df631b 20%);

}
.carousel-control-prev-icon, .carousel-control-next-icon {
    height: 50px;
    width: 50px;
    outline: black;
    background-size: 50%, 50%;
    border-radius: 50%;
    border: 1px solid white;
    filter: invert(0%);
}
.pagination>li>a{
    color: #df631b;
}

.project-tab {
    padding: 10%;
    margin-top: -8%;
}
.project-tab #tabs{
    background: #007b5e;
    color: #eee;
}
.project-tab #tabs h6.section-title{
    color: #eee;
}
.project-tab #tabs .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
    color: #df631b;
    background-color: transparent;
    border-color: transparent transparent #f3f3f3;
    border-bottom: 3px solid !important;
    font-size: 16px;
    font-weight: bold;
}
.project-tab .nav-link {
    border: 1px solid transparent;
    border-top-left-radius: .25rem;
    border-top-right-radius: .25rem;
    color: #df631b;
    font-size: 16px;
    font-weight: 600;
}
.project-tab .nav-link:hover {
    border: none;
}
.project-tab thead{
    background: #f3f3f3;
    color: #333;
}
.project-tab a{
    text-decoration: none;
    color: rgb(141, 139, 139);
    font-weight: 600;
}
.table, td{
    color:rgb(141, 139, 139)
}
.tab-pane, td{
    background-color: #333;
}

.pagination>li>a { 
    
    border-radius: 50% !important;
    margin: 0 5px;
}
.pagination { 
    
    justify-content: center;
}
.bgrand{
    background-color: black;
}

</style>
