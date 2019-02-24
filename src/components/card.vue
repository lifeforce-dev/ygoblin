<template>
    <div class="main">
        <v-content>
            <v-btn color="info" id="get-data" @click="getData">Get Data</v-btn>
        </v-content>
        <header id="header">
            <a href="#">YGoblin</a>
        </header>
        <main>
            <section id="card-info">
                <h1>Stuff</h1>
                <ul>
                    <li>
                        <span>
                            <strong>Price:</strong>
                        </span>
                    </li>
                    <li>
                        <span>
                            <strong>Attribute:</strong>
                        </span>
                    </li>
                </ul>
            </section>

            <section id="primary">
                <h1>Stuff can go here too</h1>
            </section>
        </main>
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
            this.imgUrl =
                'https://storage.googleapis.com/ygoprodeck.com/' +
                'pics/61665245.jpg';
        }
    }
};
</script>

<style lang="scss" scoped>
@import '../sass/global/card.scss';
</style>
