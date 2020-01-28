import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RestauranteComponent } from './restaurante/restaurante.component';
import { TrabalheConoscoComponent } from './trabalhe-conosco/trabalhe-conosco.component';
import { CoreComponent } from './core/core.component';
import { ContatoComponent } from './contato/contato.component';
import { BlogComponent } from './blog/blog.component';


const routes: Routes = [
  {path: '', component: CoreComponent},
  {path: 'restaurante', component: RestauranteComponent},
  {path: 'trabalhe-conosco', component: TrabalheConoscoComponent},
  {path: 'contato', component: ContatoComponent},
  {path: 'blog', component: BlogComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { };
export const routingComponents = [RestauranteComponent, TrabalheConoscoComponent, CoreComponent, ContatoComponent, BlogComponent];

