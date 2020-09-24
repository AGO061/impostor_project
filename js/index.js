var config={
    type: Phaser.AUTO,
    width:1920,
    height: 1080,
    scene:{
	preload: preload,
	create: create,
	update: update
    }

 };
var game = new Phaser.Game(config);

function preload() {
   this.load.image('map', '../maps/sheld.png');
   this.load.spritesheet('playerSprite', '../animazioni/3D/Run_begin/3D_spritesheet_run_begin.png', { frameWidth: 64, frameHeight: 64 } );
}

function create() {
    this.add.image(0,0,'map').setOrigin(0,0);
}

function update() {
    //
}
