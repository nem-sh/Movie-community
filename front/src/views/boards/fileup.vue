<template>
  <div class="container">
      <br>
      <br>
      <br>
      <br>
      <br>
      <img src="" alt="">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'
  export default {
      name:'fileup',
    /*
      Defines the data used by the component
    */
    data(){
      return {

        img: '',
        name:'dfs',
        movies: null

      }
    },

    methods: {
      /*
        Submits the file to the server
      */
      submitFile(){
        /*
                Initialize the form data
            */
            let formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('img', this.img);
            formData.append('name', this.name);

        /*
          Make the request to the POST /single-file URL
        */
            axios.post( `${BACK_URL}/boards/test/`,
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },
      testt() {
            
            axios.get(`${BACK_URL}/boards/testt`)
                .then((response) => {
                    console.log(response)
                    this.movies = response.data
                    
            })
        },

      /*
        Handles a change on the file upload
      */
      handleFileUpload(){
        this.img = this.$refs.file.files[0];
      }
    },
    created(){
        this.testt()
    },
  }
</script>