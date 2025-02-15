import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";

// Componentes
import { Home } from "./pages/Home/Home.component";
import { Mensagens } from "./pages/Mensagens/Mensagens.component";
import { Login } from "./pages/Login/Login.component"; // Standalone Component
import { Equipe } from "./pages/Equipe/Equipe.component"; // Standalone Component
import { LoginSemRedeSocial } from "./pages/LoginSemRedeSocial/LoginSemRedeSocial.component"; // Standalone Component
import { CasamentoAlice } from "./pages/CasamentoAlice/CasamentoAlice.component"; // Standalone Component
import { Kanban } from "./pages/Kanban/Kanban.component"; // Standalone Component

// Módulos extras
import { HttpClientModule } from "@angular/common/http"; // Import necessário para chamadas HTTP
import { FormsModule, ReactiveFormsModule } from "@angular/forms"; // Import para formulários

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule, // Adicionado para comunicação com backend
    FormsModule, // Para formulários tradicionais
    ReactiveFormsModule, // Para formulários reativos
    Login,
    Equipe,
    LoginSemRedeSocial,
    CasamentoAlice,
    Mensagens,
    Home,
    Kanban
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
