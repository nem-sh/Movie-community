<template>
        
        <div    class="card d-inline-block  mr-2 ml-2" v-on:mouseover = "change" v-on:mouseout = "original" style="margin-top: 80px;  background-color: black; height:300px; width:202px" @click="enterMovieDetail">
            <div v-if="changed" :class="{aactive : changed ,iinactive : !changed}" :src="getPosterPath" class=" cardimg" alt=""  style="height : 300px ;"><p style="margin-top:100px">{{movie.title}}</p></div>
            
            <img v-else :class="{aactive : changed ,iinactive : !changed}" :src="getPosterPath" class=" cardimg" alt=""  style="height : 300px ;">

            
                
        
            
            
        </div>
        
  
</template>

<script>
export default {
    name: 'MovieListUnit',
    data () {
        return{
            changed : false
        }

    },

    props:{
        movie: Object,
        modal: Boolean,
    },

    methods:{
        enterMovieDetail: function (){
            this.$router.push(`/boards/${this.movie.id}`)
        },
        change: function() {
        this.changed = true;
        },
        original: function() {
        this.changed = false;
        }
    },
    computed: {
        getPosterPath: function () {
            return `https://image.tmdb.org/t/p/w154/${this.movie.poster_path}`
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
    height: 250px;
}
.aactive {
    color : hotpink;
}
.iinactive {
    color : black;
    opacity: 1;
}

</style>