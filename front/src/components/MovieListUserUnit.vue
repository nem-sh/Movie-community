<template>
        
        <div class="card max-small d-inline-block bg-light mr-2 ml-2">
            <img src="../assets/user_basic.jpg" class="card-img-top cardimg" alt="" v-if="!movie.img">
            <img :src="getImg" class="card-img-top cardimg" alt="" v-if="movie.img">
            
            <div class="card-body p-0" style="width : 200px;">
                <h5 class="card-title">{{movie.username}}</h5>
                <p class="card-text m-0">그의 한마디.. : {{movie.one_thing}}</p>
                <a @click="intoProfile" class="btn btn-primary">Go profile</a>
            </div>
        </div>
        
  
</template>

<script>

const BACK_URL = 'http://127.0.0.1:8000'
export default {
    name: 'MovieListUnit',
    data () {
        return{
            changed : true
        }

    },

    props:{
        movie: Object,
    },

    methods:{
        
        change: function() {
        this.changed = false;
        },
        original: function() {
        this.changed = true;
        },
        intoProfile: function(){
            this.$router.push(`/accounts/profile/${this.movie.id}`)
        }
    },
    computed: {
        getImg: function () {
            return `${BACK_URL}${this.movie.img}`
        },
        
    },
    
        
    
}
</script>

<style>
.max-small2 {
    width: 280px; height: auto;
    max-height: 330px;

}
.max-small {
    width: 200px; height: auto;
    max-height: 300px;

}
.cardimg {
    width: 195px; height: 200px;
}
</style>