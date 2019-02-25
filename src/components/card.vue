<template>
    <div class="main">
        <v-content>
            <v-btn color="info" id="get-data" @click="getData">Get Data</v-btn>
        </v-content>
        <h1 id="header">YGoblin</h1>
        <v-img id="card-img" :src="imgUrl"></v-img>
    </div>
</template>

<script>
export default {
    name: 'card',
    data() {
        return {
            imgUrl: ''
        };
    },
    methods: {
        getData() {
            this.imgUrl = this.getImageUrl(61665245);
        },
        getImageUrl(id) {
            return `https://storage.googleapis.com/ygoprodeck.com/pics/${id}.jpg`;
        }
    }
};
</script>

<style lang="scss" scoped>
@import "../sass/global/card.scss";
</style>
