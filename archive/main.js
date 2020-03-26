import anime from '//unpkg.com/animejs@3.0.1/lib/anime.es.js';

// https://ptsjs.org/
const TAU = Math.PI * 2;

const canvas = document.querySelector('.js-draw');

class Stage {
  constructor(canvas, width, height) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');

    this.width = width;
    this.height = height;

    this.options = {
      rotation: Math.atan2(width, height) + Math.PI / 2,
      backgroundColor: '#011627',
      lineColor: '#FDFFFC',
      pointColor1: '#41EAD4',
      pointColor2: '#F71735',
    };

    this.points = [];

    this.line = { from: { x: 0, y: height * 0.5 }, to: { x: width, y: height * 0.5 } };

    this.animation = null;
  }

  get rotation() {
    return this.options.rotation;
  }

  get width() {
    return this.canvas.width;
  }

  get height() {
    return this.canvas.height;
  }

  get hypo() {
    return Math.hypot(this.width, this.height);
  }

  get widthHalf() {
    return this.width * 0.5;
  }

  get heightHalf() {
    return this.height * 0.5;
  }

  set width(w) {
    this.canvas.width = w;
  }

  set height(h) {
    this.canvas.height = h;
  }

  init() {
    this.generate();

    this.canvas.addEventListener('mousemove', e => this.onMouseMove(e));
    this.canvas.addEventListener('mouseenter', e => this.onMoueEnter(e));
    this.canvas.addEventListener('mouseleave', e => this.onMouseLeave(e));
  }

  generate() {
    this.points = new Array(100).fill().map((_, i) => {
      const r = (this.heightHalf * 0.5) + Math.random() * (this.heightHalf / 2);
      const c = i % 2 === 0 ? this.options.pointColor1 : this.options.pointColor2;

      const point = {
        r,
        a: Math.random() * TAU,
        s: 0.0005 + (Math.random() * 0.0008),
        c,
      };

      return point;
    });
  }

  setSize(w, h) {
    this.width = w;
    this.height = h;
  }

  onMouseMove(e) {
    const x = e.clientX - e.target.offsetLeft;
    const y = e.clientY - e.target.offsetTop;

    this.options.rotation = Math.atan2(this.heightHalf - y, this.widthHalf - x);
  }

  onMoueEnter() {
    if (this.animation) {
      this.animation.pause();
    }

    this.animation = null;
  }

  onMouseLeave() {
    this.animate();
  }

  animate() {
    const diff = -Math.PI + (Math.random() * TAU);
    const angle = this.rotation + diff;

    this.animation = anime({
      targets: this.options,
      duration: 3000,
      delay: 3000,
      rotation: angle,
      easing: 'easeInOutSine',
      complete: () => {
        this.animate();
      },
    });
  }

  drawLine(from, to, color, width = 1) {
    this.ctx.strokeStyle = color;

    this.ctx.beginPath();
    this.ctx.lineWidth = width;
    this.ctx.moveTo(from.x, from.y);
    this.ctx.lineTo(to.x, to.y);
    this.ctx.stroke();
    this.ctx.closePath();
  }

  drawPoint(point) {
    const { from, to } = this.line;
    const wh = this.canvas.width * 0.5;
    const hh = this.canvas.height * 0.5;

    point.a += point.s;
    point.x = wh + (Math.cos(point.a) * point.r);
    point.y = hh + (Math.sin(point.a) * point.r);

    const denominator = Math.hypot(to.x - from.x, to.y - from.y);
    const numerator = ((to.y - from.y) * point.x) - ((to.x - from.x) * point.y) + (to.x * from.y) - (to.y * from.x);
    const distance = numerator / denominator;

    const pointAngle = Math.atan2(to.y - from.y, to.x - from.x) + (Math.PI / 2);
    const pointRadius = 0.5 + Math.abs(distance / this.heightHalf) * 3;
    const lineWidth = 0.5 + (Math.abs(distance / this.heightHalf) - 0.5);

    const toX = point.x + (Math.cos(pointAngle) * distance);
    const toY = point.y + (Math.sin(pointAngle) * distance);

    this.ctx.save();
    this.ctx.globalAlpha = point.o;
    this.drawLine(point, { x: toX, y: toY }, this.options.lineColor, lineWidth);
    this.ctx.restore();

    this.ctx.beginPath();
    this.ctx.fillStyle = point.c;
    this.ctx.arc(point.x, point.y, pointRadius, 0, TAU);
    this.ctx.fill();
    this.ctx.closePath();
  };

  updateSeparator() {
    this.line.from.x = this.widthHalf + (Math.cos(this.rotation) * this.width);
    this.line.from.y = this.heightHalf + (Math.sin(this.rotation) * this.width);
    this.line.to.x = this.widthHalf + (Math.cos(this.rotation + Math.PI) * this.width);
    this.line.to.y = this.heightHalf + (Math.sin(this.rotation + Math.PI) * this.width);
  }

  run() {
    this.ctx.globalCompositeOperation = 'source-over';
    this.ctx.fillStyle = this.options.backgroundColor;
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    this.updateSeparator();

    this.points.forEach((p, i) => this.drawPoint(p, i));

    this.ctx.save();
    this.ctx.translate(this.widthHalf, this.heightHalf);
    this.ctx.rotate(this.rotation);
    this.ctx.globalCompositeOperation = 'difference';
    this.ctx.fillStyle = this.options.lineColor;
    this.ctx.fillRect(-this.hypo / 2, 0, this.hypo, this.hypo);
    this.ctx.restore();

    const circleRadius = 10;
    this.ctx.beginPath();
    this.ctx.fillStyle = '#fce9d5';
    this.ctx.arc(this.widthHalf, this.heightHalf, circleRadius, 0, TAU);
    this.ctx.fill();
    this.ctx.closePath();

    const circleRadiusInner = circleRadius * 0.5;
    this.ctx.beginPath();
    this.ctx.fillStyle = this.options.backgroundColor;
    this.ctx.arc(this.widthHalf, this.heightHalf, circleRadiusInner, 0, TAU);
    this.ctx.fill();
    this.ctx.closePath();

    requestAnimationFrame(() => this.run());
  }
}

const stage = new Stage(canvas, window.innerWidth, window.innerHeight);

stage.init();
stage.run();


window.addEventListener('resize', () => {
  stage.setSize(window.innerWidth, window.innerHeight);
  stage.generate();
});
