<template>
<div class="">
    <div class="container" style="height: 100%">
        <div class= "justify-content-md-center p-10" id = "title">
            묘수 풀이
        </div>
        <div class= "row h-full self-center">
            <div class= "col-md-4">
                <b-button variant="primary" block router :to="{ name: 'TrickSolveWun' }">
                    운월
                    <img src="../../assets/img/solvingTrick/wunWall.png" alt="" class="my-2">
                </b-button>
            </div>
            <div class= "col-md-4">
                <b-button variant="secondary" block router :to="{ name: 'TrickSolvePo' }">
                    포월
                    <img src="../../assets/img/solvingTrick/poWall.png" alt="" class="my-2">
                </b-button>
            </div>
            <div class= "col-md-4">
                <b-button variant="danger" block router :to="{ name: 'TrickSolveWha' }">
                    화월
                    <img src="../../assets/img/solvingTrick/hwaWall.png" alt="" class="my-2">
                </b-button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
</script>
<style scoped>
    #title{
        font-size: 40px;
    }
</style>
