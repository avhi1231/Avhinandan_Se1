import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Header from './components/headers/Header';
import Navbar from './components/navbar/Navbar';
import Subscription from './components/subscription/Subscription';
import Footer from './components/footers/Footer';
import FeaturedCategories from './components/Cat/FeaturedCategories';
function App() {
  return (
    <>
    <Header/>
    <Navbar/>
    <Subscription/>
    <FeaturedCategories/>
    <Footer/>
    </>
  );
}

export default App;
