<template>
<div class="bx--grid">
  <div class="bx--row">
    <div class="bx--col-lg-13 bx--offset-lg-3">
        <h3 class="bx--data-table-header">Packages in {{ $route.params.channel_id }}</h3>
        <cv-data-table
          :columns="columns" :data="data" ref="table"></cv-data-table>

    </div>
  </div>
</div>
</template>

<script>
  export default {

    /*  {
    "name": "channel0",
    "description": "Description of channel0",
    "private": false
  },
    */
    data: function () {
      return {
        columns: [],
        data: [],
        loading: true
      }
    },
    methods: {
      fetchData: function() {
        return fetch("/api/channels/" + this.$route.params.channel_id + "/packages").then((msg) => {
          return msg.json().then((decoded) => {
              console.log(decoded);
              this.columns = ["Name", "Description"];
              this.data = decoded.map((el) => [el.name, el.description]);
          });
        });
      }
    },
    created: function() {
      this.fetchData();
    },
}
</script>

<style>
html {
   height: 100%;
}

body, #app {
   min-height: 100%;
}

</style>
